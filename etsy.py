from random import shuffle

from sqlalchemy import desc

import requests

import json

import re

from model import User, Movie, Color, Ensemble, Cache, connect_to_db, db

etsy_api_key = "w4kl15san4n93vl9sc0b01m8"

def get_from_cache(key):

    # deleting 5 cache results
    #old_results = Cache.query.filter(Cache.created_at ).order_by(asc(Cache.created_at)).limit(5).all()
    #db.session.delete(old_results)
    #db.session.commit()

    cache_result = Cache.query.filter(Cache.key == key).first()

    if cache_result == None:
        return None
    return cache_result.value


def cache(key, value):
    """Instantiating new cached results."""
    new_cache_result = Cache(key=key, value=value)
    db.session.add(new_cache_result)
    db.session.commit()


def cached_get(url):
    """Get cached results."""
    value = get_from_cache(url)

    if value:
        return json.loads(value), 200

    response = requests.get(url)

    if response.status_code != 200:
        return None, response.status_code
        
    response_json = response.json() 
    cache(url, response.text)
    return response_json, response.status_code

def get_results(color, etsy_category, accuracy=10):
    """Getting the search results from Etsy."""
    
    # Create template url for all list item urls.
    item_url_template = (
        'https://openapi.etsy.com/v2/listings/active?color={}&color_accuracy=' +
        str(accuracy) +
        '&limit=10&sort_on=score&category={}&api_key=' +
        etsy_api_key
    )

    url = item_url_template.format(color, etsy_category)
    print 'Requesting', url
    j, status_code = cached_get(url)
    if status_code != 200:
        print 'Problem fetching', url
        return []
    if 'results' not in j or len(j['results']) == 0:
        print 'Problem - no results in ', url
        return get_results(color, etsy_category, accuracy + 20)
    return j['results']


def get_listing_items(color_list):
    """Getting search results from Wes Anderson color palettes."""

    # Shuffle the color list.
    shuffle(color_list)
    print "color list", color_list

    # Get the first five items outof the shuffled color list.
    top_color, bottom_color, shoe_color, accessory_color, bag_color = color_list[:5]

    # Getting dict results from Etsy urls.
    return dict(
        # top color results
        shirt_results=get_results(top_color, "clothing/shirt"),
        jacket_results=get_results(top_color, "clothing/jacket"),
        sweatshirt_results=get_results(top_color, "clothing/sweatshirt"),
        tank_results=get_results(top_color, "clothing/tank"),
        dress_results=get_results(top_color, "clothing/dress"),

        # bottom color results
        pants_results=get_results(bottom_color, "clothing/pants"),
        skirt_results=get_results(bottom_color, "clothing/skirt"),
        shorts_results=get_results(bottom_color, "clothing/shorts"),

        # shoe color results
        shoe_results=get_results(shoe_color, "clothing/shoes"),
        socks_results=get_results(shoe_color, "clothing/socks"),

        # accessory color results
        accessory_results=get_results(accessory_color, "accessories"),
        jewelry_results=get_results(accessory_color, "jewelry"),

        # bag color results
        bag_results=get_results(bag_color, "bags_and_purses"),
    )


def get_search_results(result_dict):
    """Create search results by categories."""
    
    accessory_results = (result_dict['accessory_results'][:10] 
                        + result_dict['jewelry_results'][:10])

    shuffle(accessory_results)

    bag_results = result_dict['bag_results'][:20]
    shuffle(bag_results)

    dress_results = result_dict['dress_results'][:20]
    shuffle(dress_results)

    bottom_results = (result_dict['pants_results'][:6] + 
                      result_dict['skirt_results'][:6] + 
                      result_dict['shorts_results'][:6])
    shuffle(bottom_results)


    top_results = (result_dict['shirt_results'][:5] + 
                   result_dict['sweatshirt_results'][:5] + 
                   result_dict['tank_results'][:5] + 
                   result_dict['jacket_results'][:5])

    shuffle(top_results)

        
    shoe_results = (result_dict['shoe_results'][:10] +
                    result_dict['socks_results'][:10]
                    )
    shuffle(shoe_results)

    return (accessory_results,
            bag_results,
            dress_results,
            bottom_results,
            top_results,
            shoe_results)


def get_best_result(results, color=None):
    """Ruling out irrelevant listing images."""

    for result in results:
        print "inside for loop\n\n\n"
        listing_id = result["listing_id"]
        image_url_template = "https://openapi.etsy.com/v2/listings/{}/images?api_key=" + etsy_api_key
        url = image_url_template.format(listing_id)
        url_dict, status_code = cached_get(url)
        num_imgs = len(url_dict['results'])

        if num_imgs > 1:
            return result, url_dict['results'][0]["url_570xN"]
        else:
            print "rejecting bad images.", url

    return result, url_dict['results'][0]["url_570xN"]


def get_image_urls(result_dict, movie_id):
    """Creating image urls for the ensemble."""
    
    try:
        (accessory_results,
            bag_results,
            dress_results,
            bottom_results,
            top_results,
            shoe_results) = get_search_results(result_dict)

        best_results_and_img_urls = {}

        if dress_results:
            d_result, d_img_url = get_best_result(dress_results)
        else:
            # query the ensemble table for Ensemble.movie_id == movie_id
            # return the dress url
            # put it into dress_results
            # call get_best_result(dress_results)
            ensemble = Ensemble.query.filter(Ensemble.movie_id == movie_id).first()

            dress_url = ensemble.dress_url

            m = re.search(r"listing/(\d+)/", dress_url)
            
            dress_listing_id = m.groups()[0]

            print "it's working!!!!\n"

            listing_dict = {
                'listing_id' : dress_listing_id,
                'url': dress_url,
            }

            d_result, d_img_url = get_best_result([listing_dict])



        best_results_and_img_urls['dress'] = (d_result, d_img_url)

        t_result, t_img_url = get_best_result(top_results)
        best_results_and_img_urls['top'] = (t_result, t_img_url)

        bo_result, bo_img_url = get_best_result(bottom_results)
        best_results_and_img_urls['bottom'] = (bo_result, bo_img_url)

        s_result, s_img_url = get_best_result(shoe_results)
        best_results_and_img_urls['shoe'] = (s_result, s_img_url)

        a_result, a_img_url = get_best_result(accessory_results)
        best_results_and_img_urls['accessory'] = (a_result, a_img_url)

        b_result, b_img_url = get_best_result(bag_results)
        best_results_and_img_urls['bag'] = (b_result, b_img_url)

    except IndexError as e:
        print e
        
    return best_results_and_img_urls


def get_listing_urls(best_dict):
    """Get listing urls."""

    best_accessory = best_dict.get('accessory')[0]
    best_top = best_dict.get('top')[0]
    best_bottom = best_dict.get('bottom')[0]
    best_shoe = best_dict.get('shoe')[0]
    best_bag = best_dict.get('bag')[0]
    best_dress = best_dict.get('dress')[0]

    # Generate listing URLs.

    dress_listing = best_dress["url"]
    print "dress url", dress_listing

    top_listing = best_top["url"]
    print "top url", top_listing

    bottom_listing = best_bottom["url"]
    print "bottom url", bottom_listing
    
    shoe_listing = best_shoe["url"]
    print "shoe url", shoe_listing

    accessory_listing = best_accessory["url"]
    print "accessory url", accessory_listing

    bag_listing = best_bag["url"]
    print "bag url", bag_listing

    return (top_listing, bottom_listing, accessory_listing, 
            dress_listing, shoe_listing, bag_listing)


if __name__ == '__main__':

    result_dict = get_listing_items(["F1BB7B", "FD6467", "5B1A18", 
        "D67236", "E6A0C4", "C93312", "FAEFD1", "DC863B", "798E87", "C27D38", "CCC591"])

    ti, boi, si, ai, bi, di = get_image_urls(result_dict, 1)
    print "\n".join([ti, boi, si, ai, bi, di])

    tl, bol, sl, al, bl, dl = get_listing_urls(result_dict)
    print "\n".join([tl, bol, sl, al, bl, dl])

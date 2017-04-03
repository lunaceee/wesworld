from random import shuffle

import requests

etsy_api_key = "w4kl15san4n93vl9sc0b01m8"

def get_results(color, etsy_category, accuracy=10):
	# Create template url for all list item urls.
	item_url_template = (
		'https://openapi.etsy.com/v2/listings/active?color={}&color_accuracy=' +
	    str(accuracy) +
	    '&limit=10&category={}&api_key=' +
	    etsy_api_key
	)

	url = item_url_template.format(color, etsy_category)
	print 'Requesting', url
	response = requests.get(url)
	if response.status_code != 200:
		print 'Problem fetching', url
		return []
	j = response.json()
	if 'results' not in j or len(j['results']) == 0:
		print 'Problem - no results in ', url
		return get_results(color, etsy_category, accuracy + 10)
	return j['results']


def get_listing_items(color_list):
	
	# Shuffle the color list.
	shuffle(color_list)
	print "color list", color_list

	# Get the first five items outof the shuffled color list.
	top_color, bottom_color, shoe_color, accessory_color, bag_color = color_list[:5]

	# Getting dict results from Etsy urls.
	return dict(
		shirt_results = get_results(top_color, "clothing/shirt"),
		jacket_results = get_results(top_color, "clothing/jacket"),
		sweatshirt_results = get_results(top_color, "clothing/sweatshirt"),
		tank_results = get_results(top_color, "clothing/tank"),

		pants_results = get_results(bottom_color, "clothing/pants"),
		skirt_results = get_results(bottom_color, "clothing/skirt"),
		shorts_results = get_results(bottom_color, "clothing/shorts"),

		shoe_results = get_results(shoe_color, "clothing/shoes"),
		socks_results = get_results(shoe_color, "clothing/socks"),

		accessory_results = get_results(accessory_color, "accessories"),
		bag_results = get_results(bag_color, "bags_and_purses"),
		dress_results = get_results(top_color, "clothing/dresses")
	)


def get_one_image_url(listing_id):
	# create template url for listing image
	image_url_template = "https://openapi.etsy.com/v2/listings/{}/images?api_key=" + etsy_api_key
	url = image_url_template.format(listing_id)
	print "url", url
	url_response = requests.get(url)
	url_dict = url_response.json()
	img_url = url_dict["results"][0]["url_570xN"]

	return img_url


def get_image_urls(result_dict):
	
	try:
		dress_results = result_dict['dress_results']

		bottom_results = (result_dict['pants_results'] + 
						  result_dict['skirt_results'] + 
						  result_dict['shorts_results'])

		top_results = (result_dict['shirt_results'] + 
					   result_dict['sweatshirt_results'] + 
					   result_dict['tank_results'] + 
					   result_dict['jacket_results'])

		
		shoe_results = result_dict['shoe_results'] + result_dict['socks_results']

		d_img_url = get_one_image_url(dress_results[0]["listing_id"])

		t_img_url = get_one_image_url(top_results[0]["listing_id"])

		bo_img_url = get_one_image_url(bottom_results[0]['listing_id'])

		s_img_url = get_one_image_url(shoe_results[0]['listing_id'])

		a_img_url = get_one_image_url(result_dict["accessory_results"][0]["listing_id"])

		b_img_url = get_one_image_url(result_dict["bag_results"][0]["listing_id"])

	except IndexError as e:
		print e
		

	return t_img_url, bo_img_url, s_img_url, a_img_url, b_img_url, d_img_url


def get_listing_urls(result_dict):
	# Getting listing URLs
	dress_results = result_dict['dress_results']

	bottom_results = (result_dict['pants_results'] + 
						  result_dict['skirt_results'] + 
						  result_dict['shorts_results'])

	top_results = (result_dict['shirt_results'] + 
					   result_dict['sweatshirt_results'] + 
					   result_dict['tank_results'] + 
					   result_dict['jacket_results'])

	shoe_results = result_dict['shoe_results'] + result_dict['socks_results']

	# Generate listing URLs.
	dress_listing = dress_results[0]["url"]

	top_listing = top_results[0]["url"]

	bottom_listing = bottom_results[0]["url"]
	
	shoe_listing = shoe_results[0]["url"]

	accessory_listing = result_dict["accessory_results"][0]["url"]

	bag_listing = result_dict["bag_results"][0]["url"]

	return (top_listing, bottom_listing, accessory_listing, 
			dress_listing, shoe_listing, bag_listing)


if __name__ == '__main__':

	result_dict = get_listing_items(
		["F1BB7B", "FD6467", "5B1A18", "D67236", "E6A0C4", "C93312", 
		"FAEFD1", "DC863B", "798E87", "C27D38", "CCC591"])

	# print t['results'][0]
	# print bo['results']
	# print s['results'][0]
	# print a['results'][0]
	# print b['results'][0]

	ti, boi, si, ai, bi = get_image_urls(result_dict)
	print "\n".join([ti, boi, si, ai, bi])

	tl, bol, sl, al, bl = get_listing_urls(result_dict)
	print "\n".join([tl, bol, sl, al, bl])
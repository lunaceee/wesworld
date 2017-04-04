from random import shuffle

import requests

etsy_api_key = "w4kl15san4n93vl9sc0b01m8"

def get_results(color, etsy_category, accuracy=10):
	# Create template url for all list item urls.
	item_url_template = (
		'https://openapi.etsy.com/v2/listings/active?color={}&color_accuracy=' +
	    str(accuracy) +
	    '&limit=10&sort_on=score&category={}&api_key=' +
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
		return get_results(color, etsy_category, accuracy + 20)
	return j['results']


def get_listing_items(color_list):
	
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

	for result in results:
		listing_id = result["listing_id"]
		image_url_template = "https://openapi.etsy.com/v2/listings/{}/images?api_key=" + etsy_api_key
		url = image_url_template.format(listing_id)
		url_response = requests.get(url)
		url_dict = url_response.json()
		num_imgs = len(url_dict['results'])

		if num_imgs > 1:
			return result, url_dict['results'][0]["url_570xN"]
		else:
			print "rejecting bad images.", url

	return result, url_dict['results'][0]["url_570xN"]




def get_one_image_url(listing_id):
	# create template url for listing image
	image_url_template = "https://openapi.etsy.com/v2/listings/{}/images?api_key=" + etsy_api_key
	url = image_url_template.format(listing_id)
	url_response = requests.get(url)
	url_dict = url_response.json()
	img_url = url_dict["results"][0]["url_570xN"]

	return img_url


def get_image_urls(result_dict):
	
	try:
		(accessory_results,
			bag_results,
			dress_results,
			bottom_results,
			top_results,
			shoe_results) = get_search_results(result_dict)

		result, d_img_url = get_best_result(dress_results)

		result, t_img_url = get_best_result(top_results)

		result, bo_img_url = get_best_result(bottom_results)

		result, s_img_url = get_best_result(shoe_results)

		result, a_img_url = get_best_result(accessory_results)

		result, b_img_url = get_best_result(bag_results)

	except IndexError as e:
		print e
		
	return t_img_url, bo_img_url, s_img_url, a_img_url, b_img_url, d_img_url


def get_listing_urls(result_dict):
	"""Get listing urls."""

	(accessory_results,
	 bag_results,
	 dress_results,
	 bottom_results,
	 top_results,
	 shoe_results) = get_search_results(result_dict)

	# Generate listing URLs.
	dress_listing = dress_results[0]["url"]
	print "dress url", dress_listing

	top_listing = top_results[0]["url"]
	print "top url", top_listing

	bottom_listing = bottom_results[0]["url"]
	print "bottom url", bottom_listing
	
	shoe_listing = shoe_results[0]["url"]
	print "shoe url", shoe_listing

	accessory_listing = accessory_results[0]["url"]
	print "accessory url", accessory_listing

	bag_listing = bag_results[0]["url"]
	print "bag url", bag_listing

	return (top_listing, bottom_listing, accessory_listing, 
			dress_listing, shoe_listing, bag_listing)


if __name__ == '__main__':

	result_dict = get_listing_items(["F1BB7B", "FD6467", "5B1A18", 
		"D67236", "E6A0C4", "C93312", "FAEFD1", "DC863B", "798E87", "C27D38", "CCC591"])

	ti, boi, si, ai, bi, di = get_image_urls(result_dict)
	print "\n".join([ti, boi, si, ai, bi, di])

	tl, bol, sl, al, bl, dl = get_listing_urls(result_dict)
	print "\n".join([tl, bol, sl, al, bl, dl])

from random import shuffle

import requests

etsy_api_key = "w4kl15san4n93vl9sc0b01m8"


def  get_listing_items(color_list):
	
	# shuffle the color list
	shuffle(color_list)

	# get first five items outof the shuffled color list
	top_color, bottom_color, shoe_color, accessory_color, bag_color = color_list[:5]

	# create a template url for all list item urls
	item_url_template = "https://openapi.etsy.com/v2/listings/active?color={}&color_accuracy=10&limit=50&category={}&api_key=" + etsy_api_key

	top_url = item_url_template.format(top_color, "clothing/shirt")
	print "top_url", top_url
	bottom_url = item_url_template.format(bottom_color, "clothing/pants")
	skirt_url = item_url_template.format(bottom_color, "clothing/skirt")
	shoe_url = item_url_template.format(shoe_color, "clothing/shoes")
	accessory_url = item_url_template.format(accessory_color, "accessories")
	bag_url = item_url_template.format(bag_color, 'bags_and_purses')

	top_response = requests.get(top_url)
	bottom_response = requests.get(bottom_url)
	shoe_response = requests.get(shoe_url)
	accessory_response = requests.get(accessory_url)
	bag_response = requests.get(bag_url)
	skirt_response = requests.get(skirt_url)

	print top_response.status_code
	print bottom_response.status_code
	print shoe_response.status_code
	print accessory_response.status_code
	print bag_response.status_code

	top_dict = top_response.json()
	bottom_dict = bottom_response.json()
	shoe_dict = shoe_response.json()
	accessory_dict = accessory_response.json()
	bag_dict = bag_response.json()
	skirt_dict = skirt_response.json()

	return top_dict, bottom_dict, shoe_dict, accessory_dict, bag_dict, skirt_dict


def get_image_urls(top_dict, bottom_dict, shoe_dict, accessory_dict, bag_dict, skirt_dict):	
	# create template url for listing image
	image_url_template = "https://openapi.etsy.com/v2/listings/{}/images?api_key=" + etsy_api_key
	bottom_results = bottom_dict['results'] + skirt_dict['results']
	# Getting listing image URLs
	top_img_url = image_url_template.format(top_dict["results"][0]["listing_id"])
	bottom_img_url = image_url_template.format(bottom_results[0]["listing_id"]) 
	shoe_img_url = image_url_template.format(shoe_dict["results"][0]["listing_id"])
	accessory_img_url = image_url_template.format(accessory_dict["results"][0]["listing_id"])
	bag_img_url = image_url_template.format(bag_dict["results"][0]["listing_id"])

	return top_img_url, bottom_img_url, shoe_img_url, accessory_img_url, bag_img_url


def get_listing_urls(top_dict, bottom_dict, shoe_dict, accessory_dict, bag_dict, skirt_dict):
	# Getting listing URLs
	bottom_results = bottom_dict['results'] + skirt_dict['results']

	top_listing = top_dict["results"][0]["url"]
	bottom_listing = bottom_results[0]["url"]
	accessory_listing = accessory_dict["results"][0]["url"]
	shoe_listing = shoe_dict["results"][0]["url"]
	bag_listing = bag_dict["results"][0]["url"]

	return top_listing, bottom_listing, accessory_listing, shoe_listing, bag_listing

if __name__ == '__main__':
	t,bo,s,a,b,sk = get_listing_items(["F1BB7B","FD6467","5B1A18","D67236","E6A0C4"])
	print t['results'][0]
	print bo['results']
	print s['results'][0]
	print a['results'][0]
	print b['results'][0]

	ti, boi, si, ai, bi = get_image_urls(t, bo, s, a, b, sk)
	print "\n".join([ti, boi, si, ai, bi])

	tl, bol, sl, al, bl = get_listing_urls(t, bo, s, a, b, sk)
	print "\n".join([tl, bol, sl, al, bl])

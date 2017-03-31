from random import shuffle

import requests

etsy_api_key = "w4kl15san4n93vl9sc0b01m8"


def get_listing_items(color_list):
	
	# Shuffle the color list.
	shuffle(color_list)

	# Get the first five items outof the shuffled color list.
	top_color, bottom_color, shoe_color, accessory_color, bag_color = color_list[:5]

	# Create template url for all list item urls.
	item_url_template = "https://openapi.etsy.com/v2/listings/active?color={}&color_accuracy=10&limit=10&category={}&api_key=" + etsy_api_key

	# Create item urls based on template url.

	shirt_url = item_url_template.format(top_color, "clothing/shirt")
	jacket_url = item_url_template.format(top_color, "clothing/jacket")
	sweat_shirt_url = item_url_template.format(top_color, "clothing/sweatshirt")
	tank_url = item_url_template.format(top_color, "clothing/tank")


	pants_url = item_url_template.format(bottom_color, "clothing/pants")
	skirt_url = item_url_template.format(bottom_color, "clothing/skirt")
	shorts_url = item_url_template.format(bottom_color, "clothing/shorts")

	socks_url = item_url_template.format(shoe_color, "clothing/socks")
	shoe_url = item_url_template.format(shoe_color, "clothing/shoes")
	
	accessory_url = item_url_template.format(accessory_color, "accessories")
	
	bag_url = item_url_template.format(bag_color, 'bags_and_purses')

	# Query Etsy API for top items.
	print "starting shirt"
	shirt_response = requests.get(shirt_url)
	print "starting jacket"
	jacket_response = requests.get(jacket_url)
	print "starting sweatshirt"
	sweatshirt_response = requests.get(sweat_shirt_url)
	print "starting tank"
	tank_response = requests.get(tank_url)

	# Query Etsy API for bottom items.
	pants_response = requests.get(pants_url)
	skirt_response = requests.get(skirt_url)
	shorts_response = requests.get(shorts_url)

	# Query Etsy API for shoe items.
	shoe_response = requests.get(shoe_url)
	socks_response = requests.get(socks_url)

	# Query Etsy API for accessory items.
	accessory_response = requests.get(accessory_url)

	# Query Etsy API for bag items.
	bag_response = requests.get(bag_url)
	

	# print top_response.status_code
	# print bottom_response.status_code
	# print shoe_response.status_code
	# print accessory_response.status_code
	# print bag_response.status_code

	# Convert search results into json object.
	shirt_dict = shirt_response.json()
	jacket_dict = jacket_response.json()
	sweatshirt_dict = sweatshirt_response.json()
	tank_dict = tank_response.json()
	pants_dict = pants_response.json()
	skirt_dict = skirt_response.json()
	shorts_dict = shorts_response.json()
	shoe_dict = shoe_response.json()
	socks_dict = socks_response.json()
	accessory_dict = accessory_response.json()
	bag_dict = bag_response.json()
	
	return (shirt_dict,
			jacket_dict,
			sweatshirt_dict,
			tank_dict,
			pants_dict,
			skirt_dict,
			shorts_dict,
			shoe_dict,
			socks_dict,
			accessory_dict,
			bag_dict)


def get_image_urls(shirt_dict,
					jacket_dict,
					sweatshirt_dict,
					tank_dict,
					pants_dict,
					skirt_dict,
					shorts_dict,
					shoe_dict,
					socks_dict,
					accessory_dict,
					bag_dict):	
	# create template url for listing image
	image_url_template = "https://openapi.etsy.com/v2/listings/{}/images?api_key=" + etsy_api_key
	
	bottom_results = pants_dict['results'] + skirt_dict['results'] + shorts_dict['results']

	top_results = shirt_dict['results'] + jacket_dict['results'] + sweatshirt_dict['results'] + tank_dict['results']

	shoe_results = shoe_dict['results'] + socks_dict['results']

	# Getting listing image URLs
	# top_img_url = image_url_template.format(top_dict["results"][0]["listing_id"])

	top_img_url = image_url_template.format(top_results[0]["listing_id"])

	tl_response = requests.get(top_img_url)
	tl_dict = tl_response.json()
	t_img_url = tl_dict["results"][0]["url_570xN"]
	# print "top image dict", t_img_url

	bottom_img_url = image_url_template.format(bottom_results[0]["listing_id"]) 
	bol_response = requests.get(bottom_img_url)
	bol_dict = bol_response.json()
	bo_img_url = bol_dict["results"][0]["url_570xN"]


	shoe_img_url = image_url_template.format(shoe_results[0]["listing_id"])
	s_response = requests.get(shoe_img_url)
	s_dict = s_response.json()
	s_img_url = s_dict["results"][0]["url_570xN"]


	accessory_img_url = image_url_template.format(accessory_dict["results"][0]["listing_id"])
	a_response = requests.get(accessory_img_url)
	a_dict = a_response.json()
	a_img_url = a_dict["results"][0]["url_570xN"]


	bag_img_url = image_url_template.format(bag_dict["results"][0]["listing_id"])
	b_response = requests.get(bag_img_url)
	b_dict = b_response.json()
	b_img_url = b_dict["results"][0]["url_570xN"]


	return t_img_url, bo_img_url, s_img_url, a_img_url, b_img_url


def get_listing_urls(shirt_dict,
					jacket_dict,
					sweatshirt_dict,
					tank_dict,
					pants_dict,
					skirt_dict,
					shorts_dict,
					shoe_dict,
					socks_dict,
					accessory_dict,
					bag_dict):
	# Getting listing URLs
	bottom_results = pants_dict['results'] + skirt_dict['results'] + shorts_dict['results']

	top_results = shirt_dict['results'] + jacket_dict['results'] + sweatshirt_dict['results'] + tank_dict['results']

	shoe_results = shoe_dict['results'] + socks_dict['results']

	# Generate listing URLs.
	top_listing = top_results[0]["url"]

	bottom_listing = bottom_results[0]["url"]
	
	shoe_listing = shoe_results[0]["url"]

	accessory_listing = accessory_dict["results"][0]["url"]

	bag_listing = bag_dict["results"][0]["url"]

	return top_listing, bottom_listing, accessory_listing, shoe_listing, bag_listing


if __name__ == '__main__':

	(shirt_dict,
	jacket_dict,
	sweatshirt_dict,
	tank_dict,
	pants_dict,
	skirt_dict,
	shorts_dict,
	shoe_dict,
	socks_dict,
	accessory_dict,
	bag_dict) = get_listing_items(
		["F1BB7B", "FD6467", "5B1A18", "D67236", "E6A0C4", "C93312", 
		"FAEFD1", "DC863B", "798E87", "C27D38","CCC591"])

	# print t['results'][0]
	# print bo['results']
	# print s['results'][0]
	# print a['results'][0]
	# print b['results'][0]

	ti, boi, si, ai, bi = get_image_urls(
										shirt_dict,
										jacket_dict,
										sweatshirt_dict,
										tank_dict,
										pants_dict,
										skirt_dict,
										shorts_dict,
										shoe_dict,
										socks_dict,
										accessory_dict,
										bag_dict)
	print "\n".join([ti, boi, si, ai, bi])

	tl, bol, sl, al, bl = get_listing_urls(
										shirt_dict,
										jacket_dict,
										sweatshirt_dict,
										tank_dict,
										pants_dict,
										skirt_dict,
										shorts_dict,
										shoe_dict,
										socks_dict,
										accessory_dict,
										bag_dict)
	print "\n".join([tl, bol, sl, al, bl])

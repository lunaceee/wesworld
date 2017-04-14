"""Utility file to seed wesworld database from seed_data/"""

from sqlalchemy import func
from model import Movie, User, Color, Ensemble, Accessory, Top, Bottom, Shoe, Bag, Dress, connect_to_db, db
from server import app
import datetime



movies = [
  {
    'name': 'The Grand Budapest Hotel', # 0
    'colors': [
        '5B1A18',
        '7294D4',
        'C6CDF7',
        'D67236',
        'D8A499',
        'E6A0C4',
        'F1BB7B',
        'FD6467'
    ],
    'top_data': {
        'listing_url':'https://www.etsy.com/listing/167182786/womens-mirror-mirror-mandala-tank-top?utm_source=wesworld&amp;utm_medium=api&amp;utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/019/0/8036514/il_570xN.518213701_kqwh.jpg'
    },
    'bottom_data': {
        'listing_url':'https://www.etsy.com/listing/292964183/harem-pants-baggy-trousers-houndstooth?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/135/1/12445613/il_570xN.1018100469_cgr8.jpg'
    },
    'accessory_data': {
        'listing_url':'https://www.etsy.com/listing/260065161/rustic-engagement-ring-box-rustic?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/101/2/8315119/il_570xN.886762880_5fjx.jpg'
    },
    'shoe_data': {
        'listing_url':'https://www.etsy.com/listing/524130745/handmade-leather-shoes-yellow-womens?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/179/1/9590072/il_570xN.1225754797_oxi3.jpg'
    },
    'bag_data': {
        'listing_url':'https://www.etsy.com/listing/523640983/ostrich-skin-ladies-handbag?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/163/0/13653028/il_570xN.1176930284_oad1.jpg'
    },
    'dress_data': {
        'listing_url':'https://www.etsy.com/listing/195258498/on-sale-womens-ladies-genevive-cut-out?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/169/0/6503545/il_570xN.1175072536_ooye.jpg'
    }
  },
  
  {
    'name': 'Bottle Rocket', # 1
    'colors': [
		'0C1707',
		'1E1E1E',
		'273046',
		'354823',
		'3F5151',
		'4E2A1E',
		'550307',
		'5F5647',
		'9B110E',
		'A42820',
		'CB2314',
		'FAD510'
    ],

    'top_data': {
        'listing_url':'https://www.etsy.com/listing/477152566/super-rare-40-acres-and-a-mule-basic-90s?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/179/2/6986150/il_570xN.1124999437_f4qv.jpg'
    },
    'bottom_data': {
        'listing_url':'https://www.etsy.com/listing/509664392/vintage-blue-indigo-cotton-twill-french?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/167/1/8591697/il_570xN.1176448692_53jm.jpg'
    },
    'accessory_data': {
        'listing_url':'https://www.etsy.com/listing/174103830/baltic-amber-dangle-earrings-leaves?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/030/1/6516418/il_570xN.544721995_5qa1.jpg'
    },
    'shoe_data': {
        'listing_url':'https://www.etsy.com/listing/253160183/yellow-and-orange-crochet-lion-booties?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/113/0/5853714/il_570xN.855854824_a738.jpg'
    },
    'bag_data': {
        'listing_url':'https://www.etsy.com/listing/495711390/emergency-food-stash?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/165/0/13524254/il_570xN.1133921968_av05.jpg'
    },
    'dress_data': {
        'listing_url':'https://www.etsy.com/listing/494866967/bohemian-wedding-dress-fringe-low-back?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/155/0/9088884/il_570xN.1211208989_8xgq.jpg'
    }
  },

  {
    'name': 'Fantastic Mr. Fox', # 3
    'colors': [
		'46ACC8',
		'B40F20',
		'DD8D29',
		'E2D200',
		'E58601',
    ],
    'top_data': {
        'listing_url':'https://www.etsy.com/listing/174662033/i-said-yes-bride-wedding-tank-top-pink?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/037/1/8171053/il_570xN.546715048_kmxf.jpg'
    },
    'bottom_data': {
        'listing_url':'https://www.etsy.com/listing/498395090/dhoti-pants?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/144/0/13745087/il_570xN.1188698007_sqa5.jpg'
    },
    'accessory_data': {
        'listing_url':'https://www.etsy.com/listing/510616686/custom-3-layering-necklace-payment-1-of?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/177/0/9636518/il_570xN.1179425352_om8x.jpg'
    },
    'shoe_data': {
        'listing_url':'https://www.etsy.com/listing/503559246/flip-flop-sock-pedicure-sock-yoga?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/144/1/8985778/il_570xN.1178418246_1luj.jpg'
    },
    'bag_data': {
        'listing_url':'https://www.etsy.com/listing/510864828/real-nappa-leather-bag-made-in-italy?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/170/0/14969467/il_570xN.1180161098_1oz5.jpg'
    },
    'dress_data': {
        'listing_url':'https://www.etsy.com/listing/130232608/custom-hand-knitted-spring-dress?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/009/0/7840131/il_570xN.454232032_efup.jpg'
    }
  },

  {
    'name': 'Moonrise Kingdom', # 4
    'colors': [
		'24281A',
		'29211F',
		'798E87',
		'85D4E3',
		'9C964A',
		'C27D38',
		'CCC591',
		'CDC08C',
		'CEAB07',
		'D5D5D3',
		'F3DF6C',
		'F4B5BD',
		'FAD77B'
    ],
    'top_data': {
        'listing_url': 'https://www.etsy.com/listing/167182786/womens-mirror-mirror-mandala-tank-top?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/019/0/8036514/il_570xN.518213701_kqwh.jpg'
    },
    'bottom_data': {
        'listing_url':'https://www.etsy.com/listing/292964183/harem-pants-baggy-trousers-houndstooth?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/135/1/12445613/il_570xN.1018100469_cgr8.jpg'
    },
    'accessory_data': {
       'listing_url':'https://www.etsy.com/listing/260065161/rustic-engagement-ring-box-rustic?utm_source=wesworld&utm_medium=api&utm_campaign=api',
       'img_url':'https://img0.etsystatic.com/101/2/8315119/il_570xN.886762880_5fjx.jpg'
    },
    'shoe_data': {
       'listing_url':'https://www.etsy.com/listing/524130745/handmade-leather-shoes-yellow-womens?utm_source=wesworld&utm_medium=api&utm_campaign=api',
       'img_url':'https://img1.etsystatic.com/179/1/9590072/il_570xN.1225754797_oxi3.jpg'
    },
    'bag_data': {
      'listing_url':'https://www.etsy.com/listing/523640983/ostrich-skin-ladies-handbag?utm_source=wesworld&utm_medium=api&utm_campaign=api',
      'img_url':'https://img0.etsystatic.com/163/0/13653028/il_570xN.1176930284_oad1.jpg'
    },
    'dress_data': {
       'listing_url':'https://www.etsy.com/listing/195258498/on-sale-womens-ladies-genevive-cut-out?utm_source=wesworld&utm_medium=api&utm_campaign=api',
       'img_url':'https://img0.etsystatic.com/169/0/6503545/il_570xN.1175072536_ooye.jpg'
    }
  },

  {
    'name': 'Rushmore', # 5
    'colors': [
		'0B775E',
		'35274A',
		'E1BD6D',
		'EABE94',
		'F2300F'
    ],
    'top_data': {
       'listing_url':'https://www.etsy.com/listing/199223565/red-slouchy-texas-love-sweatshirt?utm_source=wesworld&utm_medium=api&utm_campaign=api',
       'img_url':'https://img1.etsystatic.com/041/0/6117890/il_570xN.637767433_gzyz.jpg'
    },
    'bottom_data': {
         'listing_url':'https://www.etsy.com/listing/194654557/a-line-skirt-orange-and-red-flower-skirt?utm_source=wesworld&utm_medium=api&utm_campaign=api',
         'img_url':'https://img1.etsystatic.com/035/0/5370824/il_570xN.620777701_on4g.jpg'
    },
    'accessory_data': {
        'listing_url':'https://www.etsy.com/listing/481357699/japanese-toho-110-seed-bead-opaque?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/156/0/5962273/il_570xN.1095428990_9pau.jpg'
    },
    'shoe_data': {
        'listing_url':'https://www.etsy.com/listing/173247933/blue-felt-boots-wool-felted-boots-with?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/035/1/6751546/il_570xN.553803636_6338.jpg'
    },
    'bag_data': {
        'listing_url':'https://www.etsy.com/listing/488168367/yellow-batik-cotton-fabric-ladies-wallet?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/145/0/6879872/il_570xN.1117335289_qdth.jpg'
    },
    'dress_data': {
       'listing_url':'https://www.etsy.com/listing/167772739/bridesmaid-dress-infinity-dress-floor?utm_source=wesworld&utm_medium=api&utm_campaign=api',
       'img_url':'https://img1.etsystatic.com/038/1/8300780/il_570xN.520407539_f5a9.jpg'
    }
  },

  {
    'name': 'The Darjeeling Limited', # 6
    'colors': [
		'000000',
		'00A08A',
		'046C9A',
		'5BBCD6',
		'ABDDDE',
		'D69C4E',
		'ECCBAE',
		'F2AD00',
		'F98400',
		'FF0000'
    ],
    'top_data': {
        'listing_url':'https://www.etsy.com/listing/483852616/clearance-fried-green-tomato-t-shirt?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/150/1/6817606/il_570xN.1192865939_gssx.jpg'
    },
    'bottom_data': {
        'listing_url':'https://www.etsy.com/listing/483414711/vintage-70s-jogging-short-shorts-orange?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/101/0/5236909/il_570xN.1102698321_qexp.jpg'
    },
    'accessory_data': {
        'listing_url':'https://www.etsy.com/listing/506375158/custom-color-pet-fluffies-cat-size?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/162/0/14848666/il_570xN.1166669562_dpzn.jpg'
    },
    'shoe_data': {
        'listing_url':'https://www.etsy.com/listing/506849738/strawberry-women-socks-lady-socks-fruit?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/158/0/14625174/il_570xN.1168047154_l2h7.jpg'
    },
    'bag_data': {
        'listing_url':'https://www.etsy.com/listing/495459220/custom-hen-party-iron-on-transfer-a5?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/164/0/9373259/il_570xN.1133256766_b52z.jpg'
    },
    'dress_data': {
        'listing_url':'https://www.etsy.com/listing/93937990/oscar-worthy-coral-appliqued-silk?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/000/1/5367944/il_570xN.315544676.jpg'
    }
  },

  {
    'name': 'The Life Aquatic with Steve Zissou', # 7
    'colors': [
		'3B9AB2',
		'78B7C5',
		'E1AF00',
		'EBCC2A',
		'F21A00'
    ],
    'top_data': {
        'listing_url':'https://www.etsy.com/listing/210818026/antonio-gates-officially-licensed-nflpa?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/054/0/8840437/il_570xN.681132370_8so9.jpg'
    },
    'bottom_data': {
        'listing_url':'https://www.etsy.com/listing/474013564/vintage-apron-vintage-textiles-clothing?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/159/0/13125509/il_570xN.1068679516_kg9a.jpg'
    },
    'accessory_data': {
        'listing_url':'https://www.etsy.com/listing/491316779/japanese-toho-80-seed-bead-transparent?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/179/0/5962273/il_570xN.1141642157_1rdj.jpg'
    },
    'shoe_data': {
       'listing_url':'https://www.etsy.com/listing/508627256/blue-felted-wool-baby-booties?utm_source=wesworld&utm_medium=api&utm_campaign=api',
       'img_url':'https://img0.etsystatic.com/144/0/12180002/il_570xN.1173386246_d0k1.jpg'
    },
    'bag_data': {
        'listing_url':'https://www.etsy.com/listing/488168367/yellow-batik-cotton-fabric-ladies-wallet?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/145/0/6879872/il_570xN.1117335289_qdth.jpg'
    },
    'dress_data': {
        'listing_url':'https://www.etsy.com/listing/98094869/vintage-inspired-retro-rockabilly-swing?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/000/0/6303914/il_570xN.330651855.jpg'
    }
  },

  {
    'name': 'The Royal Tenenbaums', # 8
    'colors': [
		'74A089',
		'899DA4',
		'9A8822',
		'C93312',
		'DC863B',
		'F5CDB4',
		'F8AFA8',
		'FAEFD1',
		'FDDDA0'
    ],
    'top_data': {
        'listing_url': 'https://www.etsy.com/listing/507179447/on-sale-unisex-adult-sport-jacket-adidas?utm_source=wesworld&amp;utm_medium=api&amp;utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/157/0/13847946/il_570xN.1174474673_jt1f.jpg'
    },
    'bottom_data': {
         'listing_url': 'https://www.etsy.com/listing/98391465/ice-queen-bustle-burlesque-tie-on?utm_source=wesworld&utm_medium=api&utm_campaign=api',
         'img_url':'https://img1.etsystatic.com/000/0/5799614/il_570xN.331727309.jpg'
    },
    'accessory_data': {
        'listing_url':'https://www.etsy.com/listing/221499543/japanese-necklacejapanese-embossed-paper?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/049/0/8001507/il_570xN.723066248_lg65.jpg'
    },
    'shoe_data': {
       'listing_url': 'https://www.etsy.com/listing/477655381/monsters-inc-inspired-baby-booties?utm_source=wesworld&utm_medium=api&utm_campaign=api',
       'img_url':'https://img0.etsystatic.com/109/0/13673049/il_570xN.1040255616_bj4r.jpg'
    },
    'bag_data': {
        'listing_url': 'https://www.etsy.com/listing/522602563/yellow-african-print-coin-purse-zipper?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img1.etsystatic.com/144/0/14921729/il_570xN.1221162327_1572.jpg'
    },
    'dress_data': {
        'listing_url': 'https://www.etsy.com/listing/181565936/historical-clothing-for-ed?utm_source=wesworld&utm_medium=api&utm_campaign=api',
        'img_url':'https://img0.etsystatic.com/030/0/9090359/il_570xN.572373226_srq9.jpg'
    }
  }
]


def load_users():
    """Load users from u.user into database."""

    print "Users"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    User.query.delete()

    # Read user_data file and insert data
    for row in open("seed_data/user_data.txt"):
        row = row.rstrip()
        user_id, username, email, password = row.split("|")

        user = User(
                    username=username,
                    email=email,
                    password=password
                    )

        # We need to add to the session or it won't ever be stored
        db.session.add(user)

    # Once we're done, we should commit our work
    db.session.commit()



def load_movies_colors_items_ensembles():
    """Load movies from movie_data into database."""
    print "moives, colors, items, ensembles"
    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate movies
    Movie.query.delete()
    Color.query.delete()
    Accessory.query.delete()
    Top.query.delete()
    Bottom.query.delete()
    Shoe.query.delete()
    Bag.query.delete()
    Dress.query.delete()

    for movie_dict in movies:
    	movie = Movie(
                      name=movie_dict['name'],
                     )
    	db.session.add(movie)
    	db.session.commit()
    	for hexcode in movie_dict['colors']:
    		color = Color(
                       hexcode=hexcode,
                       movie_id=movie.id
                       )
    		db.session.add(color)
        accessory = Accessory(listing_url=movie_dict['accessory_data']['listing_url'],
                    img_url=movie_dict['accessory_data']['img_url'])
        db.session.add(accessory)

        top = Top(listing_url=movie_dict['top_data']['listing_url'],
                    img_url=movie_dict['top_data']['img_url'])
        db.session.add(top)

        bottom = Bottom(listing_url=movie_dict['bottom_data']['listing_url'],
                    img_url=movie_dict['bottom_data']['img_url'])
        db.session.add(bottom)

        shoe = Shoe(listing_url=movie_dict['shoe_data']['listing_url'],
                    img_url=movie_dict['shoe_data']['img_url'])
        db.session.add(shoe)

        bag = Bag(listing_url=movie_dict['bag_data']['listing_url'],
                    img_url=movie_dict['bag_data']['img_url'])
        db.session.add(bag)

        dress = Dress(listing_url=movie_dict['dress_data']['listing_url'],
                    img_url=movie_dict['dress_data']['img_url'])
        db.session.add(dress)

        db.session.commit()

        ensemble = Ensemble(
                            accessory_id=accessory.id,
                            top_id=top.id,
                            bottom_id=bottom.id,
                            shoe_id=shoe.id,
                            bag_id=bag.id,
                            dress_id=dress.id,
                            movie_id=movie.id
                            )
        db.session.add(ensemble)

    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_users()
    load_movies_colors_items_ensembles()

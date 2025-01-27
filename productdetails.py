import cherrypy

class ProductPage:
    @cherrypy.expose
    def index(self, id=None):
        products = {
            # Home products
            "running-shoes": {
                "name": "Running Shoes",
                "price": "999",
                "description": "High-performance running shoes for athletes.",
                "features": ["Breathable material", "Lightweight", "Durable sole"],
                "image": "https://m.media-amazon.com/images/I/71f3BmjCwtL._AC_UY1000_.jpg",
            },
            "adjustable-dumbbells": {
                "name": "Adjustable Dumbbells",
                "price": "1500",
                "description": "Adjustable dumbbells for versatile workouts.",
                "features": ["Compact design", "Multiple weights", "Durable material"],
                "image": "https://www.ukgymequipment.com/images/2-5-50kg-premium-urethane-dumbbell-set-p5790-75425_image.jpg",
            },
            "dumbbell-set": {
                "name": "Dumbbell set",
                "price": "1499",
                "description": "Adjustable dumbbells for versatile workouts.",
                "features": ["Compact design", "Multiple weights", "Durable material"],
                "image": "https://m.media-amazon.com/images/I/612wD806BnL._AC_UL320_.jpg",
            },
            "mountain-bike": {
                "name": "Mountain Bike",
                "price": "2500",
                "description": "Adjustable dumbbells for versatile workouts.",
                "features": ["Compact design", "Multiple weights", "Durable material"],
                "image": "https://bicyclewarehouse.com/cdn/shop/products/giant-fathom-1-27-5-mountain-bike-2022-28685815382118.jpg",
            },
            "treadmill": {
                "name": "Treadmill",
                "price": "20000",
                "description": "Adjustable dumbbells for versatile workouts.",
                "features": ["Compact design", "Multiple weights", "Durable material"],
                "image": "https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg",
            },
            "protein-bar": {
                "name": "Protein Bar",
                "price": "800",
                "description": "Adjustable dumbbells for versatile workouts.",
                "features": ["Compact design", "Multiple weights", "Durable material"],
                "image": "https://www.bigbasket.com/media/uploads/p/xl/40122051_8-ritebite-max-protein-daily-choco-almond-bar.jpg",
            },
            "cricket-set": {
                "name": "Cricket Set",
                "price": "1000",
                "description": "Adjustable dumbbells for versatile workouts.",
                "features": ["Compact design", "Multiple weights", "Durable material"],
                "image": "https://m.media-amazon.com/images/I/61U5D3Cm0OL._AC_UF894,1000_QL80_.jpg",
            },
            
            # All Categories Page products
            "yoga-mat": {
                "name": "Yoga Mat",
                "price": "700",
                "description": "Durable and anti-slip yoga mat for a comfortable workout.",
                "features": ["Anti-slip", "Lightweight", "Eco-friendly material"],
                "image": "https://m.media-amazon.com/images/I/61iLVerCzOL._SX569_.jpg"
            },
            "resistance-bands": {
               "name": "Resistance Bands",
               "price": "500",
               "description": "Versatile resistance bands for strength training.",
               "features": ["High elasticity", "Portable", "Durable"],
               "image": "https://m.media-amazon.com/images/I/612c73jZt1L._SX569_.jpg"
            },
            "skipping-rope": {
               "name": "Skipping Rope",
               "price": "200",
               "description": "Durable skipping rope for cardiovascular exercise.",
               "features": ["Adjustable length", "Ergonomic handles", "Tangle-free design"],
               "image": "https://m.media-amazon.com/images/I/81O6gfeClDL._SX569_.jpg"
            },
            "foam-roller": {
               "name": "Foam Roller",
               "price": "800",
               "description": "High-density foam roller for muscle recovery.",
               "features": ["High durability", "Compact design", "Ideal for deep tissue massage"],
               "image": "https://m.media-amazon.com/images/I/41gZtYEhabL._AC_UL320_.jpg"
            },
            "ankle-weights": {
               "name": "Ankle Weights",
               "price": "450",
               "description": "Adjustable ankle weights for resistance training.",
               "features": ["Adjustable straps", "Comfortable fit", "Durable fabric"],
               "image": "https://m.media-amazon.com/images/I/41b81SJr4dL._AC_UL320_.jpg"
            },
            "mountain-bike": {
               "name": "Mountain Bike",
               "price": "1299",
               "description": "Durable mountain bike for outdoor adventures.",
               "features": ["Strong frame", "High-traction tires", "Smooth gear shifting"],
               "image": "https://bicyclewarehouse.com/cdn/shop/products/giant-fathom-1-27-5-mountain-bike-2022-28685815382118.jpg"
            },
            "treadmill": {
               "name": "Treadmill",
               "price": "20000",
               "description": "High-performance treadmill for indoor running.",
               "features": ["Multiple speed settings", "Foldable design", "Digital display"],
               "image": "https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg"
            },
           "protein-bar": {
               "name": "Protein Bar",
               "price": "800",
               "description": "Nutrient-packed protein bar for post-workout recovery.",
               "features": ["Rich in protein", "Low in sugar", "Tasty and healthy"],
               "image": "https://www.bigbasket.com/media/uploads/p/xl/40122051_8-ritebite-max-protein-daily-choco-almond-bar.jpg"
            },
           "gym-bag": {
               "name": "Gym Bag",
               "price": "370",
               "description": "Spacious and durable gym bag for carrying essentials.",
               "features": ["Water-resistant material", "Adjustable straps", "Compact and lightweight"],
               "image": "https://m.media-amazon.com/images/I/815CS0qdoyL._SX569_.jpg"
            },
            "leather-gym-gloves": {
               "name": "Leather Gym Gloves",
               "price": "399",
               "description": "Comfortable leather gloves for gym workouts.",
               "features": ["Breathable material", "Enhanced grip", "Wrist support"],
               "image": "https://m.media-amazon.com/images/I/71WllQEscmL._SX569_.jpg"
            },
            "sports-running-set": {
               "name": "Sports Running Set",
               "price": "494",
               "description": "Complete running outfit for athletes.",
               "features": ["Breathable fabric", "Comfortable fit", "Lightweight"],
               "image": "https://m.media-amazon.com/images/I/41g3uCT1OpL.jpg"
            },
            "gym-knee-cap": {
              "name": "Gym Knee Cap",
              "price": "189",
              "description": "Supportive knee cap for gym and fitness activities.",
              "features": ["Elastic material", "Durable design", "Comfortable fit"],
              "image": "https://m.media-amazon.com/images/I/71r5YHLuOdL._SX679_PIbundle-2,TopRight,0,0_AA679SH20_.jpg"
            },
            "gym-typhoon-shaker": {
               "name": "Boldfit Plastic Gym Typhoon Shaker",
               "price": "179",
               "description": "Durable plastic shaker for mixing protein shakes.",
               "features": ["Leak-proof design", "BPA-free material", "Easy to clean"],
               "image": "https://m.media-amazon.com/images/I/51NKPZx0a6L._SX569_.jpg"
            },
            "sports-sunglasses": {
                "name": "Sports Sunglasses",
                "price": "1049",
                "description": "Stylish and protective sunglasses for outdoor activities.",
                "features": ["UV protection", "Lightweight frame", "Anti-glare lenses"],
                "image": "https://m.media-amazon.com/images/I/61GG2gHjlDL._SX679_.jpg"
            },
            "weight-plate": {
             "name": "Weight Plate",
             "price": "579",
             "description": "High-quality weight plate for strength training.",
             "features": ["Durable material", "Compatible with most bars", "Non-slip surface"],
             "image": "https://m.media-amazon.com/images/I/61NU+Lr-ZzL._SX569_.jpg"
            },
            "adjustable-dumbbells": {
               "name": "Adjustable Dumbbells",
               "price": "1500",
               "description": "Versatile dumbbells that can be adjusted for different weights.",
               "features": ["Adjustable weight plates", "Durable material", "Compact design"],
               "image": "https://www.ukgymequipment.com/images/2-5-50kg-premium-urethane-dumbbell-set-p5790-75425_image.jpg"
            },
            "treadmill": {
              "name": "Treadmill",
              "price": "20000",
              "description": "High-performance treadmill for indoor running.",
              "features": ["Multiple speed settings", "Foldable design", "Digital display"],
              "image": "https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg"
            },
            "kettlebell": {
               "name": "Kettlebell",
               "price": "800",
               "description": "Compact and versatile kettlebell for strength training.",
               "features": ["Ergonomic handle", "Durable construction", "Compact design"],
               "image": "https://m.media-amazon.com/images/I/615mcUuFzEL._SX569_.jpg"
            },
            "bench-press": {
               "name": "Bench Press",
               "price": "4500",
               "description": "Durable bench press for strength and weightlifting exercises.",
               "features": ["Adjustable incline", "Sturdy frame", "Padded seat"],
               "image": "https://m.media-amazon.com/images/I/416jU1p4hyL._SX300_SY300_QL70_FMwebp_.jpg"
            },
            "rowing-machine": {
              "name": "Rowing Machine",
              "price": "18000",
              "description": "Full-body workout machine with smooth rowing motion.",
              "features": ["Adjustable resistance", "Digital display", "Compact design"],
              "image": "https://m.media-amazon.com/images/I/61waH3MGrSL._AC_UY218_.jpg"
            },
            "gym-and-fitness-kit": {
               "name": "Gym And Fitness Kit",
               "price": "1299",
               "description": "Comprehensive kit for home fitness enthusiasts.",
               "features": ["Multiple tools", "Compact storage", "High-quality materials"],
               "image": "https://m.media-amazon.com/images/I/81XNzjmXi+L._SX569_.jpg"
            },
            "hand-gripper": {
               "name": "Hand Gripper",
               "price": "169",
               "description": "Portable hand gripper for strengthening grip muscles.",
               "features": ["Adjustable resistance", "Compact design", "Durable construction"],
               "image": "https://m.media-amazon.com/images/I/61WCHJEB05L._SX569_.jpg"
            },
            "gymnastic-rings": {
               "name": "Gymnastic Rings",
               "price": "1599",
               "description": "Durable gymnastic rings for bodyweight training.",
               "features": ["Adjustable straps", "Sturdy design", "Non-slip grip"],
               "image": "https://m.media-amazon.com/images/I/41p9Y5lD1JL._SX300_SY300_QL70_FMwebp_.jpg"
            },
            "gym-bag": {
               "name": "Gym Bag",
               "price": "370",
               "description": "Spacious and durable gym bag for carrying essentials.",
               "features": ["Water-resistant material", "Adjustable straps", "Compact and lightweight"],
               "image": "https://m.media-amazon.com/images/I/815CS0qdoyL._SX569_.jpg"
            },
            "dumbbell": {
               "name": "Dumbbell",
               "price": "1568",
               "description": "Durable dumbbell for strength training.",
               "features": ["Non-slip grip", "Compact design", "High-quality materials"],
               "image": "https://m.media-amazon.com/images/I/31hnntmHgmL.jpg"
            },
            "vinyl-kettlebell": {
               "name": "Vinyl Kettlebell",
               "price": "1599",
               "description": "Vinyl-coated kettlebell for versatile strength exercises.",
               "features": ["Ergonomic handle", "Durable vinyl coating", "Compact size"],
               "image": "https://m.media-amazon.com/images/I/6116etN+S-L._SX569_.jpg"
            },
            "vinyl-dumbbells": {
                "name": "Vinyl 4 Pound Dumbbells",
                "price": "829",
                "description": "Lightweight vinyl dumbbells for strength and toning.",
                "features": ["Durable coating", "Non-slip grip", "Compact size"],
                "image": "https://m.media-amazon.com/images/I/51aMp8BYasL._SX569_.jpg"
            },
            "weight-lifting-rod": {
                "name": "Weight Lifting Rod",
                "price": "599",
                "description": "High-quality weight lifting rod for strength training.",
                "features": ["Durable construction", "Non-slip grip", "Standard compatibility"],
                "image": "https://m.media-amazon.com/images/I/41-GQXTb13L._SX569_.jpg"
            },
            "pull-up-bar": {
                "name": "Pull Up Bar",
                "price": "1049",
                "description": "Sturdy pull-up bar for upper body strength training.",
                "features": ["Adjustable length", "Non-slip grip", "Easy installation"],
                "image": "https://m.media-amazon.com/images/I/616S2Q0RqjL._SX569_.jpg"
            },
            "weight-plate": {
               "name": "Weight Plate",
               "price": "579",
               "description": "Durable weight plate for strength and fitness exercises.",
               "features": ["Non-slip surface", "Standard compatibility", "High-quality material"],
               "image": "https://m.media-amazon.com/images/I/61NU+Lr-ZzL._SX569_.jpg"
            },
            "sport-sunglasses": {
              "name": "Sport Sunglasses",
              "price": "799",
              "description": "Stylish and durable sport sunglasses for outdoor activities.",
              "features": ["UV protection", "Lightweight", "Scratch-resistant lenses"],
              "image": "https://m.media-amazon.com/images/I/51du4P5G3AL._SX679_.jpg"
            },
            "sports-watch": {
              "name": "Sports Watch",
              "price": "279",
              "description": "Affordable and functional sports watch for everyday use.",
              "features": ["Water-resistant", "Digital display", "Lightweight design"],
              "image": "https://m.media-amazon.com/images/I/51BrFkZcMxL._SX679_.jpg"
            },
            "sports-archery-bow-and-arrow": {
               "name": "Sports Archery Bow and Arrow",
               "price": "399",
               "description": "Archery set for recreational use and beginner practice.",
               "features": ["Lightweight design", "Durable material", "Safe for kids"],
               "image": "https://m.media-amazon.com/images/I/61kWpOTZYIL._SX466_.jpg"
            },
            "kids-bowling-play-set": {
               "name": "Kids Bowling Play Set",
               "price": "356",
               "description": "Bowling play set for kids to develop coordination and skills.",
               "features": ["Colorful pins", "Lightweight balls", "Durable design"],
               "image": "https://m.media-amazon.com/images/I/81jxG+mj+ZL._SY450_.jpg"
            },
            "dart-boards": {
              "name": "Dart Boards",
              "price": "499",
              "description": "Compact dartboard for recreational and practice use.",
              "features": ["Magnetic darts", "Portable design", "Safe for all ages"],
              "image": "https://m.media-amazon.com/images/I/513y-y80AOL._SX300_SY300_QL70_FMwebp_.jpg"
            },
            "cricket-set": {
              "name": "Cricket Set",
              "price": "1299",
              "description": "Complete cricket set for outdoor play.",
              "features": ["Lightweight bat", "Durable stumps", "High-quality ball"],
              "image": "https://m.media-amazon.com/images/I/61U5D3Cm0OL._AC_UF894,1000_QL80_.jpg"
            },
            "frisbee": {
               "name": "Frisbee",
               "price": "69",
               "description": "Lightweight and durable frisbee for outdoor fun.",
               "features": ["Aerodynamic design", "Easy to throw", "Bright colors"],
               "image": "https://m.media-amazon.com/images/I/61Q+dn494aL._SX569_.jpg"
            },
            "ludo-snakes-and-ladders": {
              "name": "Ludo + Snakes & Ladders",
              "price": "615",
              "description": "Classic board game set for family fun.",
              "features": ["Colorful board", "Compact design", "Easy to store"],
              "image": "https://m.media-amazon.com/images/I/71jfnSDekDL._SX450_.jpg"
            },
            "sudoku-brain-game": {
               "name": "Sudoku Brain Game",
               "price": "349",
               "description": "Puzzle game to challenge and improve logic skills.",
               "features": ["Portable design", "Multiple difficulty levels", "Durable material"],
               "image": "https://m.media-amazon.com/images/I/71m-JjVJNdL._SY425_.jpg"
            },
            "soccer-game-board": {
               "name": "Soccer Game Board",
               "price": "1298",
               "description": "Fun tabletop soccer game for indoor play.",
               "features": ["Compact design", "Easy to use", "Durable construction"],
               "image": "https://m.media-amazon.com/images/I/411v-HeMR-L._SX300_SY300_QL70_FMwebp_.jpg"
            },
            "string-hockey-table-board": {
               "name": "String Hockey Table Board",
               "price": "490",
               "description": "Compact string hockey table board for quick matches.",
               "features": ["Lightweight", "Portable design", "Durable build"],
               "image": "https://m.media-amazon.com/images/I/71KDPQhQ1qL._SX569_.jpg"
            },
            "basketball-hoop": {
               "name": "Basketball Hoop",
               "price": "999",
               "description": "Mini basketball hoop for indoor and outdoor use.",
               "features": ["Adjustable height", "Durable frame", "Easy setup"],
               "image": "https://m.media-amazon.com/images/I/81ndumBu4FS._SX569_.jpg"
            },
            "wooden-jigsaw-puzzle": {
              "name": "Wooden Jigsaw Puzzle",
              "price": "290",
              "description": "Classic wooden jigsaw puzzle for kids and adults.",
              "features": ["Durable wood", "Bright colors", "Multiple difficulty levels"],
              "image": "https://m.media-amazon.com/images/I/71rJwGG3jDL._SX450_.jpg"
            },
            "stress-buster-cube": {
              "name": "Stress Buster Cube",
              "price": "349",
              "description": "Portable stress-relief cube with multiple activities.",
              "features": ["Compact design", "Durable material", "Great for focus"],
              "image": "https://m.media-amazon.com/images/I/71OXrIaR0nL._SY450_.jpg"
            },
            "wooden-labyrinth-board": {
              "name": "Wooden Labyrinth Board",
              "price": "304",
              "description": "Challenging wooden labyrinth board game.",
              "features": ["Smooth surface", "Sturdy build", "Portable design"],
              "image": "https://m.media-amazon.com/images/I/71T7jVDDciL._SX450_.jpg"
            },
            "tshirt-for-men": {
              "name": "Tshirt for Men",
              "price": "598",
              "description": "Comfortable and stylish T-shirt for men, perfect for casual wear.",
              "features": ["Soft cotton fabric", "Breathable material", "Available in multiple sizes"],
              "image": "https://m.media-amazon.com/images/I/61ThK8RnMjL._SX679_.jpg"
            },
            "cotton-socks": {
                "name": "Cotton Socks",
                "price": "379",
                "description": "Premium quality cotton socks for all-day comfort.",
                "features": ["Breathable fabric", "Sweat-absorbent", "Durable material"],
                "image": "https://m.media-amazon.com/images/I/71aWx1mvCpL._SX679_.jpg"
            },
            "sports-shorts": {
                "name": "Sports Shorts",
                "price": "718",
                "description": "Lightweight sports shorts for maximum performance.",
                "features": ["Quick-dry material", "Elastic waistband", "Multiple color options"],
                "image": "https://m.media-amazon.com/images/I/51+mkAk9KeL._SX679_.jpg"
            },
            "sports-running-set": {
                "name": "Sports Running Set",
                "price": "494",
                "description": "Complete running outfit for comfort and style.",
                "features": ["Breathable fabric", "Stretchable material", "Lightweight design"],
                "image": "https://m.media-amazon.com/images/I/41g3uCT1OpL.jpg"
            },
            "line-coat": {
                "name": "Line Coat",
                "price": "1249",
                "description": "Elegant and durable line coat for men.",
                "features": ["Stylish design", "Warm material", "Perfect for formal occasions"],
                "image": "https://m.media-amazon.com/images/I/51OYFbJbwDL._SX679_.jpg"
            },
            "sipper-bottle": {
                "name": "Sipper Bottle",
                "price": "649",
                "description": "High-quality sipper bottle for hydration on the go.",
                "features": ["Leak-proof design", "Durable material", "Easy to carry"],
                "image": "https://m.media-amazon.com/images/I/81TwSqGPHDL._SX679_.jpg"
            },
            "joggers-men": {
                "name": "Joggers Men",
                "price": "389",
                "description": "Comfortable joggers for workouts and casual wear.",
                "features": ["Stretchable material", "Breathable fabric", "Elastic waistband"],
                "image": "https://m.media-amazon.com/images/I/61b+OM+VtXL._SX679_.jpg"
            },
            "pajama-pants": {
                "name": "Pajama Pants",
                "price": "499",
                "description": "Soft and cozy pajama pants for lounging.",
                "features": ["Relaxed fit", "Elastic waistband", "Durable material"],
                "image": "https://m.media-amazon.com/images/I/51lH2Qey-NL._SY741_.jpg"
            },
            "track-pants": {
                "name": "Track Pants",
                "price": "399",
                "description": "Comfortable track pants for everyday wear.",
                "features": ["Stretchable material", "Breathable fabric", "Adjustable waistband"],
                "image": "https://m.media-amazon.com/images/I/31BCg+gakIL.jpg"
            },
            "bomber-jacket": {
                "name": "Bomber Jacket",
                "price": "449",
                "description": "Trendy bomber jacket for a stylish look.",
                "features": ["Lightweight material", "Zipper closure", "Multiple color options"],
                "image": "https://m.media-amazon.com/images/I/51XWUBbfe7L._SX679_.jpg"
            },
            "digital-sports-watch": {
                "name": "Digital Sports Watch",
                "price": "790",
                "description": "Modern digital sports watch for all-day use.",
                "features": ["Water-resistant", "LED display", "Durable strap"],
                "image": "https://m.media-amazon.com/images/I/718eNAc+AAL._SY679_.jpg"
            },
            "sports-shoes": {
                "name": "Sports Shoes",
                "price": "1119",
                "description": "Durable and comfortable sports shoes for men.",
                "features": ["Non-slip sole", "Lightweight design", "Breathable material"],
                "image": "https://m.media-amazon.com/images/I/611+P1LFyWS._SY695_.jpg"
            },
            "cricket-cap": {
                "name": "Cricket Cap",
                "price": "297",
                "description": "Classic cricket cap for sun protection and style.",
                "features": ["Adjustable strap", "Durable material", "Breathable design"],
                "image": "https://m.media-amazon.com/images/I/71guHaHnSsL._SX679_.jpg"
            },
            "sports-sunglasses": {
                "name": "Sports Sunglasses",
                "price": "1299",
                "description": "Protective sports sunglasses for outdoor activities.",
                "features": ["UV protection", "Lightweight frame", "Shatterproof lenses"],
                "image": "https://m.media-amazon.com/images/I/51ViSAvmVpL._SX679_.jpg"
            },
            "cricket-helmet-skull-cap": {
               "name": "Cricket Helmet Skull Cap",
               "price": "198",
               "description": "Lightweight cricket helmet skull cap for head protection.",
               "features": ["Adjustable fit", "Durable material", "Ventilated design"],
               "image": "https://m.media-amazon.com/images/I/41xKb2Gh6OL._SX679_.jpg"
            },
            "brainvita-board-game": {
                "name": "Brainvita Board Game",
                "price": "130",
                "description": "A classic strategy board game for all ages.",
                "features": ["Engaging puzzle", "Great for strategy development", "For 1 or more players"],
                "image": "https://m.media-amazon.com/images/I/912UmK8nfWL._SY450_.jpg"
            },
            "carrom-board": {
                "name": "Carrom Board",
                "price": "1199",
                "description": "Classic indoor game for family and friends.",
                "features": ["Smooth surface", "Durable build", "Great for all ages"],
                "image": "https://m.media-amazon.com/images/I/616qmRUNOsL._SY679_.jpg"
            },
            "wireless-controller": {
                "name": "Wireless Controller",
                "price": "1746",
                "description": "Wireless gaming controller for an enhanced experience.",
                "features": ["Compatible with multiple devices", "Ergonomic design", "Long battery life"],
                "image": "https://m.media-amazon.com/images/I/31aJy+xNpZL._SY300_SX300_.jpg"
            },
            "rechargeable-hover-football": {
                "name": "Rechargeable Hover Football Indoor Game",
                "price": "499",
                "description": "Rechargeable hover football for indoor fun.",
                "features": ["Easy to charge", "Glides smoothly", "Perfect for kids and adults"],
                "image": "https://m.media-amazon.com/images/I/41E5hab325L._SX300_SY300_QL70_FMwebp_.jpg"
            },
            "tic-tac-toe": {
                "name": "Tic Tac Toe Toy Game",
                "price": "239",
                "description": "Classic Tic Tac Toe game for endless entertainment.",
                "features": ["Portable", "Great for all ages", "Fun for family and friends"],
                "image": "https://m.media-amazon.com/images/I/519XIs57j1L._SX450_.jpg"
            },
            "abs-roller": {
                "name": "Abs Roller",
                "price": "179",
                "description": "Abs roller for a full-body workout.",
                "features": ["Compact design", "Ergonomic handle", "Perfect for core exercises"],
                "image": "https://m.media-amazon.com/images/I/71Vt2Pgy4hL._SX569_.jpg"
            },
            "solitaire-board": {
                "name": "Solitaire Board in Wood",
                "price": "499",
                "description": "A wooden solitaire board for single-player challenges.",
                "features": ["Elegant wooden design", "Portable", "Great for all ages"],
                "image": "https://m.media-amazon.com/images/I/61yLb5L-P4L._SY450_.jpg"
            },
            "monopoly": {
                "name": "Monopoly",
                "price": "1499",
                "description": "The classic board game of strategy and fortune.",
                "features": ["For 2-6 players", "Engages family and friends", "Develop your property empire"],
                "image": "https://m.media-amazon.com/images/I/818p67YdM3L._SY450_.jpg"
            },
            "strategy-board-game": {
                "name": "Strategy Board Game",
                "price": "795",
                "description": "Exciting strategy game for competitive play.",
                "features": ["For 2-4 players", "Strategic gameplay", "Easy-to-learn rules"],
                "image": "https://m.media-amazon.com/images/I/51Z63aOVsgL._SX300_SY300_QL70_FMwebp_.jpg"
            },
            "badminton-racquet": {
                "name": "Badminton Racquet",
                "price": "749",
                "description": "Lightweight badminton racquet for a fun sport experience.",
                "features": ["Durable frame", "Comfortable grip", "Lightweight design"],
                "image": "https://m.media-amazon.com/images/I/81eSsR1GKyL._SX569_.jpg"
            },
            "sipper-bottle": {
                "name": "Sipper Bottle",
                "price": "899",
                "description": "Stylish sipper bottle for hydration on the go.",
                "features": ["Leak-proof design", "Portable", "Keeps your drink cool or warm"],
                "image": "https://m.media-amazon.com/images/I/71T5vGBK2OL._SX569_.jpg"
            },
            "wrist-support": {
                "name": "Wrist Support",
                "price": "179",
                "description": "Supportive wrist brace for pain relief and protection.",
                "features": ["Breathable material", "Adjustable", "Provides compression and stability"],
                "image": "https://m.media-amazon.com/images/I/51Ml+0Kx5YL._SX569_.jpg"
            },
            "soccer-ball": {
              "name": "Soccer Ball",
              "price": "329",
              "description": "High-quality soccer ball for outdoor play.",
              "features": ["Durable", "Standard size", "Perfect for practice and games"],
              "image": "https://m.media-amazon.com/images/I/61RpRYFb2wL._SX569_.jpg"
            },
          "table-tennis": {
              "name": "Table Tennis",
              "price": "640",
              "description": "Complete table tennis set for indoor fun.",
              "features": ["Includes paddles and balls", "Great for family and friends", "Durable table tennis set"],
              "image": "https://m.media-amazon.com/images/I/711H-8d-sjL._SX569_.jpg"
            },
           "jumping-rope": {
              "name": "Jumping Rope",
              "price": "99",
              "description": "Perfect skipping rope for fitness enthusiasts.",
              "features": ["Adjustable length", "Durable material", "Portable and lightweight"],
              "image": "https://m.media-amazon.com/images/I/71l2-gWOnpL._SX569_.jpg"
        },
}
        
        if not id or id not in products:
            return "<h2>Product not found</h2>"

        product = products[id]

        # Safely extract optional details
        description = product.get('description', 'No description available.')
        features = product.get('features', [])

        return f"""
        <html>
        <head>
            <title>{product['name']}</title>
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{ font-family: Arial, sans-serif; display: flex; flex-direction: column; min-height: 100vh; }}
                .product-container {{ max-width: 800px; margin: auto; flex: 1; padding: 20px; }}
                img {{ width: 100%; height: 80vh; border: 1px solid #ccc; }}
                .details {{ margin: 20px 0; }}
                .features {{ list-style: none; padding: 0; }}
                .features li {{ margin: 5px 0; }}
                button {{ background-color: #ff9900; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer; }}
                button:hover {{ background-color: #e68a00; transform: scale(1.05);}}
                .wishlist-btn {{ background-color: #007bff; }}
                .wishlist-btn:hover {{ background-color: #0056b3; transform: scale(1.05);}}
                footer {{ background-color: #333; color: white; text-align: center; padding: 10px; margin-top: auto; }}
            </style>
            <script>
                function addToCart(name, price, description, imageURL) {{
                    alert(name + " has been added to your cart!");
                    // Redirect to cart endpoint (optional)
                    window.location.href = "/cart/add?item=" + encodeURIComponent(name)+
                        "&price=" + encodeURIComponent(price) +
                        "&description=" + encodeURIComponent(description) +
                        "&imageURL=" + encodeURIComponent(imageURL);
                }}
                
                function buyNow(productName) {{
                    alert("Proceeding to buy " + productName + "!");
                    console.log("Buying:", productName);
                    window.location.href = '/checkout';
                }}

                function addToWishlist(item, price, imageUrl) {{
                    // Correctly encode parameters
                    const formattedPrice = price.replace(/[^\d.]/g, ''); // Strip ₹ or other currency symbols
                    window.location.href = '/wishlist/add?item=' + encodeURIComponent(item) + '&price=' + encodeURIComponent(formattedPrice)+ '&imageUrl=' + encodeURIComponent(imageUrl);
                }}
            </script>
        </head>
        <body>
            <div class="product-container">
                <img src="{product['image']}" alt="{product['name']}">
                <h1>{product['name']}</h1>
                <p class="details">{description}</p>
                <h2>Price: ₹{product['price']}</h2>
                <h3>Features:</h3>
                <ul class="features">
                    {"".join(f"<li>{feature}</li>" for feature in features)}
                </ul>
                <button onclick="addToCart('{product['name']}', '{product['price']}', '{description}', '{product['image']}')">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 229, 229, 1);transform: ;msFilter:;"><circle cx="10.5" cy="19.5" r="1.5"></circle><circle cx="17.5" cy="19.5" r="1.5"></circle><path d="M21 7H7.334L6.18 4.23A1.995 1.995 0 0 0 4.333 3H2v2h2.334l4.743 11.385c.155.372.52.615.923.615h8c.417 0 .79-.259.937-.648l3-8A1.003 1.003 0 0 0 21 7zm-4 6h-2v2h-2v-2h-2v-2h2V9h2v2h2v2z"></path></svg>
                </button>
                <button onclick="buyNow('{product['name']}')">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                    <path d="M16 23V4L4 7.5L3 20.5L16 23Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M17.5 5.14833L16 4V23L21 21.5C21 18.8371 20.7998 16.178 20.4012 13.5451L19.1298 5.14833H17.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M13.0016 4.87502C13.0092 2.85785 12.239 1.26304 11.0023 1.02911C9.44084 0.73373 7.72699 2.71982 7.17435 5.46517C7.09535 5.85761 7.04435 6.24433 7.01953 6.61979" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M14.8665 4.33083C14.5732 3.14854 13.9527 2.31296 13.1092 2.14837C11.7258 1.8784 10.2195 3.50662 9.55469 5.8801" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M12.7896 9.42437C11.7896 9.0035 9.19076 8.24627 8.50372 10.266C8.1332 11.3553 8.79795 12.5183 10.2171 13.6331C12.2041 15.1939 11.867 16.524 11.5033 17.0001C10.2176 18.6837 7.64621 17.7016 6.78906 17.0001" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                  </svg>
                </button>
                <button class="wishlist-btn" onclick="addToWishlist('{product['name']}', '{product['price']}', '{product['image']}')">
                   <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" style="fill:white;margin-right:5px;"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path></svg>
                </button>
            </div>
            <footer>
                <p>&copy; 2024 SportsFit. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """

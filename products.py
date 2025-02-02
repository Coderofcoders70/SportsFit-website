import cherrypy
import json

# Example data structure for products
PRODUCTS = [
    {"id": "running-shoes", "name": "Running Shoes", "category": "sports-wear", "price": 999, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/71f3BmjCwtL._AC_UY1000_.jpg"},
    {"id": "adjustable-dumbbells", "name": "Adjustable Dumbbells", "category": "gym-equipment", "price": 1500, "rating": 4.2, "image": "https://www.ukgymequipment.com/images/2-5-50kg-premium-urethane-dumbbell-set-p5790-75425_image.jpg"},
    {"id": "mountain-bike", "name": "Mountain Bike", "category": "fitness-accessories", "price": 2500, "rating": 4.5, "image": "https://bicyclewarehouse.com/cdn/shop/products/giant-fathom-1-27-5-mountain-bike-2022-28685815382118.jpg"},
    {"id": "treadmill", "name": "Treadmill", "category": "gym-equipment", "price": 20000, "rating": 4.8, "image": "https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg"},
    {"id": "protein-bar", "name": "Protein Bar", "category": "fitness-accessories", "price": 800, "rating": 4.3, "image": "https://www.bigbasket.com/media/uploads/p/xl/40122051_8-ritebite-max-protein-daily-choco-almond-bar.jpg"},
    {"id": "cricket-set", "name": "Cricket Set", "category": "sports-accessories", "price": 1000, "rating": 3.2, "image": "https://m.media-amazon.com/images/I/61U5D3Cm0OL._AC_UF894,1000_QL80_.jpg"},
    {"id": "yoga-mat", "name": "Yoga Mat", "category": "fitness-accessories", "price": 700, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/61iLVerCzOL._SX569_.jpg"},
    {"id": "resistance-bands", "name": "Resistance Bands", "category": "gym-equipment", "price": 500, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/612c73jZt1L._SX569_.jpg"},
    {"id": "medicine-ball", "name": "Rubber Gym Ball", "category": "gym-equipment", "price": 649, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/418FX6ET7-L._SX300_SY300_QL70_FMwebp_.jpg"},
    {"id": "skipping-rope", "name": "Skipping Rope", "category": "fitness-accessories", "price": 200, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/81O6gfeClDL._SX569_.jpg"},
    {"id": "foam-roller", "name": "Foam Roller", "category": "fitness-accessories", "price": 800, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/41gZtYEhabL._AC_UL320_.jpg"},
    {"id": "ankle-weights", "name": "Ankle Weights", "category": "fitness-accessories", "price": 450, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/41b81SJr4dL._AC_UL320_.jpg"},
    {"id": "cross-trainer", "name": "Cross Trainer", "category": "gym-equipment", "price": 16000, "rating": 4.8, "image": "https://m.media-amazon.com/images/I/611tsGRPkOL._SX522_.jpg"},
    {"id": "gym-bag", "name": "Gym Bag", "category": "gym-equipment", "price": 370, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/815CS0qdoyL._SX569_.jpg"},
    {"id": "leather-gym-gloves", "name": "Leather Gym Gloves", "category": "sports-wear", "price": 399, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/71WllQEscmL._SX569_.jpg"},
    {"id": "sports-running-set", "name": "Sports Running Set", "category": "sports-wear", "price": 494, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/41g3uCT1OpL.jpg"},
    {"id": "gym-knee-cap", "name": "Gym Knee Cap", "category": "sports-wear", "price": 189, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/71r5YHLuOdL._SX679_PIbundle-2,TopRight,0,0_AA679SH20_.jpg"},
    {"id": "gym-typhoon-shaker", "name": "Boldfit Plastic Gym Typhoon Shaker", "category": "sports-wear", "price": 179, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/51NKPZx0a6L._SX569_.jpg"},
    {"id": "sports-sunglasses", "name": "Sports Sunglasses", "category": "sports-wear", "price": 1049, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/61GG2gHjlDL._SX679_.jpg"},
    {"id": "weight-plate", "name": "Weight Plate", "category": "fitness-accessories", "price": 579, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/61NU+Lr-ZzL._SX569_.jpg"},
    {"id": "dumbbellset", "name": "Dumbbell set", "category": "gym-equipment", "price": 1499, "rating": 3.2, "image": "https://m.media-amazon.com/images/I/612wD806BnL._AC_UL320_.jpg"},
    {"id": "kettlebell", "name": "Kettlebell", "category": "gym-equipment", "price": 800, "rating": 2.1, "image": "https://m.media-amazon.com/images/I/615mcUuFzEL._SX569_.jpg"},
    {"id": "bench-press", "name": "Bench Press", "category": "gym-equipment", "price": 4500, "rating": 4.6, "image": "https://m.media-amazon.com/images/I/416jU1p4hyL._SX300_SY300_QL70_FMwebp_.jpg"},
    {"id": "rowing-machine", "name": "Rowing Machine", "category": "gym-equipment", "price": 18000, "rating": 3.8, "image": "https://m.media-amazon.com/images/I/61waH3MGrSL._AC_UY218_.jpg"},
    {"id": "gym-and-fitness-kit", "name": "Gym And Fitness Kit", "category": "gym-equipment", "price": 1299, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/81XNzjmXi+L._SX569_.jpg"},
    {"id": "hand-gripper", "name": "Hand Gripper", "category": "gym-equipment", "price": 169, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/61WCHJEB05L._SX569_.jpg"},
    {"id": "gymnastic-rings", "name": "Gymnastic Rings", "category": "fitness-accessories", "price": 1599, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/41p9Y5lD1JL._SX300_SY300_QL70_FMwebp_.jpg"},
    {"id": "gym-bag", "name": "Gym Bag", "category": "gym-equipment", "price": 370, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/815CS0qdoyL._SX569_.jpg"},
    {"id": "dumbbell", "name": "Dumbbell", "category": "gym-equipment", "price": 1568, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/31hnntmHgmL.jpg"},
    {"id": "vinyl-kettlebell", "name": "Vinyl Kettlebell", "category": "gym-equipment", "price": 1599, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/6116etN+S-L._SX569_.jpg"},
    {"id": "vinyl-dumbbells", "name": "Vinyl 4 Pound Dumbbells", "category": "gym-equipment", "price": 829, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/51aMp8BYasL._SX569_.jpg"},
    {"id": "weight-lifting-rod", "name": "Weight Lifting Rod", "category": "gym-equipment", "price": 599, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/41-GQXTb13L._SX569_.jpg"},
    {"id": "pull-up-bar", "name": "Pull Up Bar", "category": "gym-equipment", "price": 1049, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/616S2Q0RqjL._SX569_.jpg"},
    {"id": "weight-plate", "name": "Weight Plate", "category": "gym-equipment", "price": 579, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/61NU+Lr-ZzL._SX569_.jpg"},
    {"id": "sport-sunglasses", "name": "Sport Sunglasses", "category": "sports-accessories", "price": 799, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/51du4P5G3AL._SX679_.jpg"},
    {"id": "sports-watch", "name": "Sports Watch", "category": "sports-accessories", "price": 279, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/51BrFkZcMxL._SX679_.jpg"},
    {"id": "sports-archery-bow-and-arrow", "name": "Sports Archery Bow and Arrow", "category": "sports-collection", "price": 399, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/61kWpOTZYIL._SX466_.jpg"},
    {"id": "kids-bowling-play-set", "name": "Kids Bowling Play Set", "category": "sports-collection", "price": 356, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/81jxG+mj+ZL._SY450_.jpg"},
    {"id": "dart-boards", "name": "Dart Boards", "category": "sports-accessories", "price": 499, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/513y-y80AOL._SX300_SY300_QL70_FMwebp_.jpg"},
    {"id": "cricket-set", "name": "Cricket Set", "category": "sports-collection", "price": 1299, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/61U5D3Cm0OL._AC_UF894,1000_QL80_.jpg"},
    {"id": "frisbee", "name": "Frisbee", "category": "sports-accessories", "price": 69, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/61Q+dn494aL._SX569_.jpg"},
    {"id": "ludo-snakes-and-ladders", "name": "Ludo + Snakes & Ladders", "category": "sports-accessories", "price": 615, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/71jfnSDekDL._SX450_.jpg"},
    {"id": "sudoku-brain-game", "name": "Sudoku Brain Game", "category": "sports-accessories", "price": 349, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/71m-JjVJNdL._SY425_.jpg"},
    {"id": "soccer-game-board", "name": "Soccer Game Board", "category": "sports-accessories", "price": 1298, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/411v-HeMR-L._SX300_SY300_QL70_FMwebp_.jpg"},
    {"id": "string-hockey-table-board", "name": "String Hockey Table Board", "category": "sports-accessories", "price": 490, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/71KDPQhQ1qL._SX569_.jpg"},
    {"id": "basketball-hoop", "name": "Basketball Hoop", "category": "sports-collection", "price": 999, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/81ndumBu4FS._SX569_.jpg"},
    {"id": "wooden-jigsaw-puzzle", "name": "Wooden Jigsaw Puzzle", "category": "sports-collection", "price": 290, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/71rJwGG3jDL._SX450_.jpg"},
    {"id": "stress-buster-cube", "name": "Stress Buster Cube", "category": "sports-collection", "price": 349, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/71OXrIaR0nL._SY450_.jpg"},
    {"id": "wooden-labyrinth-board", "name": "Wooden Labyrinth Board", "category": "sports-collection", "price": 304, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/71T7jVDDciL._SX450_.jpg"},
    {"id": "tshirt-for-men", "name": "Tshirt for Men", "category": "sports-wear", "price": 598, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/61ThK8RnMjL._SX679_.jpg"},
    {"id": "cotton-socks", "name": "Cotton Socks", "category": "sports-wear", "price": 379, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/71aWx1mvCpL._SX679_.jpg"},
    {"id": "sports-shorts", "name": "Sports Shorts", "category": "sports-wear", "price": 718, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/51+mkAk9KeL._SX679_.jpg"},
    {"id": "sports-running-set", "name": "Sports Running Set", "category": "sports-wear", "price": 494, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/41g3uCT1OpL.jpg"},
    {"id": "line-coat", "name": "Line Coat", "category": "sports-wear", "price": 1249, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/51OYFbJbwDL._SX679_.jpg"},
    {"id": "sipper-bottle", "name": "Sipper Bottle", "category": "sports-wear", "price": 649, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/81TwSqGPHDL._SX679_.jpg"},
    {"id": "joggers-men", "name": "Joggers Men", "category": "sports-wear", "price": 389, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/61b+OM+VtXL._SX679_.jpg"},
    {"id": "pajama-pants", "name": "Pajama Pants", "category": "sports-wear", "price": 499, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/51lH2Qey-NL._SY741_.jpg"},
    {"id": "track-pants", "name": "Track Pants", "category": "sports-wear", "price": 399, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/31BCg+gakIL.jpg"},
    {"id": "bomber-jacket", "name": "Bomber Jacket", "category": "sports-wear", "price": 449, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/51XWUBbfe7L._SX679_.jpg"},
    {"id": "digital-sports-watch", "name": "Digital Sports Watch", "category": "accessories", "price": 790, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/718eNAc+AAL._SY679_.jpg"},
    {"id": "sports-shoes", "name": "Sports Shoes", "category": "sports-wear", "price": 1119, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/611+P1LFyWS._SY695_.jpg"},
    {"id": "cricket-cap", "name": "Cricket Cap", "category": "sports-wear", "price": 297, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/71guHaHnSsL._SX679_.jpg"},
    {"id": "sports-sunglasses", "name": "Sports Sunglasses", "category": "sports-wear", "price": 1299, "rating": 4.6, "image": "https://m.media-amazon.com/images/I/51ViSAvmVpL._SX679_.jpg"},
    {"id": "cricket-helmet-skull-cap", "name": "Cricket Helmet Skull Cap", "category": "sports-wear", "price": 198, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/41xKb2Gh6OL._SX679_.jpg"},
    {"id": "brainvita-board-game", "name": "Brainvita Board Game", "category": "sports-accessories", "price": 130, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/912UmK8nfWL._SY450_.jpg"},
    {"id": "carrom-board", "name": "Carrom Board", "category": "sports-accessories", "price": 1199, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/616qmRUNOsL._SY679_.jpg"},
    {"id": "wireless-controller", "name": "Wireless Controller", "category": "electronics", "price": 1746, "rating": 4.7, "image": "https://m.media-amazon.com/images/I/31aJy+xNpZL._SY300_SX300_.jpg"},
    {"id": "rechargeable-hover-football", "name": "Rechargeable Hover Football Indoor Game", "category": "sports-accessories", "price": 499, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/41E5hab325L._SX300_SY300_QL70_FMwebp_.jpg"},
    {"id": "tic-tac-toe", "name": "Tic Tac Toe Toy Game", "category": "sports-accessories", "price": 239, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/519XIs57j1L._SX450_.jpg"},
    {"id": "abs-roller", "name": "Abs Roller", "category": "fitness-accessories", "price": 179, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/71Vt2Pgy4hL._SX569_.jpg"},
    {"id": "solitaire-board", "name": "Solitaire Board in Wood", "category": "sports-accessories", "price": 499, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/61yLb5L-P4L._SY450_.jpg"},
    {"id": "monopoly", "name": "Monopoly", "category": "sports-accessories", "price": 1499, "rating": 4.7, "image": "https://m.media-amazon.com/images/I/818p67YdM3L._SY450_.jpg"},
    {"id": "strategy-board-game", "name": "Strategy Board Game", "category": "sports-accessories", "price": 795, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/51Z63aOVsgL._SX300_SY300_QL70_FMwebp_.jpg"},
    {"id": "badminton-racquet", "name": "Badminton Racquet", "category": "sports-collection", "price": 749, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/81eSsR1GKyL._SX569_.jpg"},
    {"id": "sipper-bottle-premium", "name": "Sipper Bottle Premium", "category": "sports-wear", "price": 899, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/71T5vGBK2OL._SX569_.jpg"},
    {"id": "wrist-support", "name": "Wrist Support", "category": "sports-wear", "price": 179, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/51Ml+0Kx5YL._SX569_.jpg"},
    {"id": "soccer-ball", "name": "Soccer Ball", "category": "sports", "price": 329, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/61RpRYFb2wL._SX569_.jpg"},
    {"id": "table-tennis", "name": "Table Tennis", "category": "sports-accessories", "price": 640, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/711H-8d-sjL._SX569_.jpg"},
    {"id": "jumping-rope", "name": "Jumping Rope", "category": "fitness-accessories", "price": 99, "rating": 4.0, "image": "https://m.media-amazon.com/images/I/71l2-gWOnpL._SX569_.jpg"},
    {"id": "men-tshirt", "name": "Men's T-Shirt", "category": "men", "price": 499, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/61ThK8RnMjL._SX679_.jpg"},
    {"id": "men-gym-gloves", "name": "Men's Gym Gloves", "category": "men", "price": 1599, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/71WllQEscmL._SX522_.jpg"},
    {"id": "men-trackpants", "name": "Men's Trackpants", "category": "men", "price": 799, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/61IK6hKv-2L._AC_UL320_.jpg"},
    {"id": "men-belt", "name": "Men's Belt ", "category": "men", "price": 999, "rating": 4.6, "image": "https://m.media-amazon.com/images/I/81rOh-82ZUL._SX679_.jpg"},
    {"id": "men-solid-shorts", "name": "Dry Fit Solid Shorts", "category": "men", "price": 1299, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/71Bo5j9n2vL._SX522_.jpg"},
    {"id": "men-shoes", "name": "Men's Shoes", "category": "men", "price": 2199, "rating": 4.7, "image": "https://m.media-amazon.com/images/I/61KpvTZtczL._SY695_.jpg"},
    {"id": "men-cap", "name": "Men's Cap", "category": "men", "price": 399, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/61F348t3NML._SX569_.jpg"},
    {"id": "men-backpack", "name": "Men's Backpack", "category": "men", "price": 1799, "rating": 4.6, "image": "https://m.media-amazon.com/images/I/81t7HX8bmAL._AC_UL320_.jpg"},
    {"id": "men-wrist-watch", "name": "Men's Watch", "category": "men", "price": 2999, "rating": 4.8, "image": "https://m.media-amazon.com/images/I/51AYRQ-s-qL._AC_UL320_.jpg"},
    {"id": "men-compression-tshirt", "name": "Half Sleeve Compression TShirt", "category": "men", "price": 699, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/51ageXP6o3L._SY679_.jpg"},
    {"id": "women-gym-sleeves", "name": "Women's Long Sleeve Tank Tops", "category": "women", "price": 1299, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/61T5+PGIeRL._SX522_.jpg"},
    {"id": "women-sports-bra", "name": "Sports Bra Fitness", "category": "women", "price": 999, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/41QhLtrFLBL.jpg"},
    {"id": "women-shoes", "name": "Women's Running Shoes", "category": "women", "price": 1599, "rating": 4.6, "image": "https://m.media-amazon.com/images/I/51tP3oO3HuL._SY575_.jpg"},
    {"id": "women-yoga-pants", "name": "Stretchable Yoga Pants", "category": "women", "price": 1099, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/419kJyD7GzL._SX679_.jpg"},
    {"id": "women-gym-bag", "name": "Fabric Gym Bag", "category": "women", "price": 1999, "rating": 4.8, "image": "https://m.media-amazon.com/images/I/613lYX6kqzL._SX569_.jpg"},
    {"id": "women-watch", "name": "Smart Watch", "category": "women", "price": 2999, "rating": 4.7, "image": "https://m.media-amazon.com/images/I/418tFshxkJL._SX300_SY300_QL70_FMwebp_.jpg"},
    {"id": "women-shorts", "name": "Yoga Shorts", "category": "women", "price": 899, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/71SZ77E2NxL._SX569_.jpg"},
    {"id": "women-headbands", "name": "Sports Headband", "category": "women", "price": 1299, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/41RuHlfZpiL.jpg"},
    {"id": "women-handbands", "name": "Wrist Band", "category": "women", "price": 1599, "rating": 4.7, "image": "https://m.media-amazon.com/images/I/61gdqE1y2vL._SX522_.jpg"},
    {"id": "women-hair-clips", "name": "Clutchers Clips", "category": "women", "price": 299, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/71w4nwreaXL._SX695_.jpg"},
    {"id": "women-hair-serum", "name": "Hair Serum", "category": "women", "price": 299, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/31QRILb+aZL._SY300_SX300_.jpg"},
    {"id": "kids-tshirt", "name": "Kid's T-Shirt", "category": "kids", "price": 499, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/71novhku+XL._SX679_.jpg"},
    {"id": "kids-shoes", "name": "Kid's Shoes", "category": "kids", "price": 799, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/617iSvrz4iL._SY575_.jpg"},
    {"id": "kids-shorts", "name": "Boys & Girls Sports Shorts", "category": "kids", "price": 899, "rating": 4.5, "image": "https://m.media-amazon.com/images/I/61n0jvStvPL._SX679_.jpg"},
    {"id": "kids-tracksuit", "name": "Track Suit", "category": "kids", "price": 1099, "rating": 4.6, "image": "https://m.media-amazon.com/images/I/81iCPGSMhCL._SX679_.jpg"},
    {"id": "kids-watch", "name": "Kid's Watch", "category": "kids", "price": 599, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/71SJCUPqVPL._SX679_.jpg"},
    {"id": "kids-table-tennnis", "name": "Table Tennis", "category": "kids", "price": 299, "rating": 4.2, "image": "https://m.media-amazon.com/images/I/51sMfjay-VL._SX522_.jpg"},
    {"id": "kids-rubber-ball", "name": "Rubber Hop Ball", "category": "kids", "price": 1299, "rating": 4.6, "image": "https://m.media-amazon.com/images/I/41K5Q+JPQQL._SX425_.jpg"},
    {"id": "kids-toys", "name": "Kid's Toys", "category": "kids", "price": 499, "rating": 4.4, "image": "https://m.media-amazon.com/images/I/51ecKyKK-VL._SX300_SY300_QL70_FMwebp_.jpg"},
    {"id": "kids-writing-pad", "name": "Writing Pad for Drawing, Playing, Handwriting Gifts for Kids", "category": "kids", "price": 199, "rating": 4.1, "image": "https://m.media-amazon.com/images/I/51nzIs6jTCL._SX425_.jpg"},
    {"id": "kids-gloves", "name": "Kid's Gloves", "category": "kids", "price": 399, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/61GnSS3fKPL._SY679_.jpg"},
    {"id": "kids-skatesboard", "name": "Skateboard set", "category": "kids", "price": 399, "rating": 4.3, "image": "https://m.media-amazon.com/images/I/81T3i2BJSsL._SX522_.jpg"}
]

class Products:

    @cherrypy.expose
    def index(self, category=None, price_range=None, min_rating=None):
        """
        Display products with optional filters for category, price range, and rating.
        """
        filtered_products = PRODUCTS

        # Filter products
        if category:
            filtered_products = [p for p in filtered_products if p['category'] == category]

        if price_range:
            try:
                min_price, max_price = map(int, price_range.split('-'))
                filtered_products = [p for p in filtered_products if min_price <= p['price'] <= max_price]
            except ValueError:
                pass

        if min_rating:
            try:
                min_rating = float(min_rating)
                filtered_products = [p for p in filtered_products if p['rating'] >= min_rating]
            except ValueError:
                pass

        # Generate HTML for filtered products
        products_html = "".join(
            f"""
            <div class='product'>
                <img src='{product['image']}' alt='{product['name']}' />
                <h3>{product['name']}</h3>
                <p>Price: ₹{product['price']}</p>
                <p>
                    Rating: {''.join(['<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" style="fill:gold;"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path></svg>' for _ in range(int(product['rating']))])}
                </p>
                <button onclick="addToCart('{product['id']}','{product['price']}', '{product['category']}', '{product['image']}')">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 229, 229, 1);transform: ;msFilter:;"><circle cx="10.5" cy="19.5" r="1.5"></circle><circle cx="17.5" cy="19.5" r="1.5"></circle><path d="M21 7H7.334L6.18 4.23A1.995 1.995 0 0 0 4.333 3H2v2h2.334l4.743 11.385c.155.372.52.615.923.615h8c.417 0 .79-.259.937-.648l3-8A1.003 1.003 0 0 0 21 7zm-4 6h-2v2h-2v-2h-2v-2h2V9h2v2h2v2z"></path></svg>
                </button>
                <button onclick="addToWishlist('{product['id']}', '{product['price']}', '{product['image']}')">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" style="fill:white;margin-right:5px;"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path></svg>
                </button>
            </div>
            """ for product in filtered_products
        )

        # Preserve selected filters
        category_options = "".join(
            f"<option value='{cat}' {'selected' if cat == category else ''}>{cat.replace('-', ' ').title()}</option>"
            for cat in ["All", "fitness-accessories", "gym-equipment", "sports-wear", "sports-accessories", "men", "women", "kids"]
        )
        price_options = "".join(
            f"<option value='{range_}' {'selected' if range_ == price_range else ''}>{label}</option>"
            for range_, label in [
                ("", "All"),
                ("0-1000", "Under ₹1000"),
                ("1000-2000", "₹1000 - ₹2000"),
                ("2000-5000", "₹2000 - ₹5000"),
                ("5000-10000", "₹5000 - ₹10000"),
                ("10000-30000", "₹10000 - ₹30000"),
            ]
        )
        rating_value = min_rating if min_rating else 0

        return f"""
        <!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title>Product Page</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; }}
                .header {{
                    width: 100%;
                    background-color: #333;
                    color: white;
                    padding: 20px 0;
                    text-align: center;
                    font-size: 42px;
                    font-family: sans-serif;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    margin-bottom: 30px;
                }}
                .header_img{{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }}
                .container {{ display: flex; }}
                .filters {{ width: 20%; padding: 20px; background: #fff; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }}
                .products {{ width: 70%; display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 20px; padding: 20px; }}
                .product {{ background: white; padding: 30px; border: 1px solid #ccc; border-radius: 8px;  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); }}
                .product img {{ width: 100%; border-bottom: 1px solid #ccc; margin-bottom: 10px; }}
                .filters h3 {{ margin-bottom: 10px; }}
                .filter-group {{ margin-bottom: 20px; }}
                .filter-group label {{ display: block; margin-bottom: 5px; font-size: 20px; font-family: sans-serif; font-weight: bold; }}
                .filter-group input, .filter-group select {{ width: 100%; padding: 5px; font-size: 16px; margin-bottom: 10px; }}
                .filter-group input[type='range'] {{ width: 100%; }}
                button {{ padding: 10px; background: #333; color: white; font-size: 18px; border: none; border-radius: 5px; cursor: pointer;}}
                button:hover {{ background: #555; transform: scale(1.05);}}
                .back-home {{ text-align: center; text-decoration: none; font-size:25px; color: #333; margin-top: 20px; }}
                .back-home a{{text-decoration: none; color: #333;}}
                .back-home:hover{{text-decoration: underline;}}
                footer {{
                    background-color: #232f3e;
                    color: white;
                    padding: 30px;
                    font-family: Arial, sans-serif;
                }}
                footer {{ background-color: #333; color: white; text-align: center; padding: 80px; margin-top: 50px;}}
                .footer-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 20px;
                    margin-bottom: 20px;
                }}

                .footer-grid h3 {{
                    font-size: 25px;
                    margin-bottom: 10px;
                    border-bottom: 1px solid #3a45533;
                    padding-bottom: 5px;
                }}

                .footer-grid ul {{
                    list-style: none;
                    padding: 0;
                }}

                .footer-grid ul li {{
                    margin: 5px 0;
                }}

                .footer-grid ul li a {{
                    color: #ddd;
                    text-decoration: none;
                    font-size: 19px;
                    line-height: 40px;
                }}
                .footer-grid ul li a:hover {{
                    color: white;
                    text-decoration: underline;
                }}
                .footer-bottom {{
                    text-align: center;
                    border-top: 1px solid #3a4553;
                    padding-top: 5px;
                    font-size: 20px;
                    line-height: 80px;
                    width: 88vw;
                }}
                .footer-bottom svg{{
                    margin: -5px;
                    width: 50px;
                }}
            </style>
            <script>
                function addToCart(productId) {{
                    alert('Added to Cart: ' + productId);
                }}
                function addToCart(productName, price, category, imageURL) {{
                    alert(productName + " has been added to your cart!");
                    window.location.href = "/cart/add?item=" + encodeURIComponent(productName) +
                          "&price=" + encodeURIComponent(price) +
                          "&category=" + encodeURIComponent(category) +
                          "&imageURL=" + encodeURIComponent(imageURL);
                }}
                function addToWishlist(productId) {{
                    alert('Added to Wishlist: ' + productId);
                }}
                function addToWishlist(name, price, imageUrl) {{
                    window.location.href = "/wishlist/add?item=" + encodeURIComponent(name) + "&price=" + encodeURIComponent(price)+
                    "&imageUrl=" + encodeURIComponent(imageUrl);
                }}
            </script>
        </head>
        <body>
        <div class="header">Products</div>
           <div class= "header_img">
            <img src='https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Topbanner/New/new-banner-GIF-1500x300.gif' alt='' />
           </div>
            <div class='container'>
                <div class='filters'>
                    <form method='get' action='/products'>
                        <div class='filter-group'>
                            <label for='category'>Category:</label>
                            <select name='category' id='category'>
                                {category_options}
                            </select>
                        </div>
                        <div class='filter-group'>
                            <label for='price_range'>Price:</label>
                            <select name='price_range' id='price_range'>
                                {price_options}
                            </select>
                        </div>
                        <div class='filter-group'>
                            <label for='min_rating'>Rating:⭐⭐⭐⭐⭐</label>
                            <input type='range' name='min_rating' id='min_rating' min='0' max='5' step='0.1' value='{rating_value}'>
                        </div>
                        <button type='submit'>Apply filters</button>
                    </form>
                </div>
                <div class='products'>
                    {products_html if filtered_products else '<p>No products found matching the filters.</p>'}
                </div>
            </div>
            <div class="back-home">
             <a href="/">Back To Home</a>
            </div>
            <footer>
                <div class="footer-grid">
            <!-- Section: Get to Know Us -->
            <div>
                <h3>Get to Know Us</h3>
                <ul>
                    <li><a href="#">About SportsFit</a></li>
                    <li><a href="#">Careers</a></li>
                    <li><a href="#">Press Releases</a></li>
                    <li><a href="#">SportsFit Science</a></li>
                </ul>
            </div>

            <!-- Section: Connect with Us -->
            <div>
                <h3>Connect with Us</h3>
                <ul>
                    <li><a href="#">Facebook</a></li>
                    <li><a href="#">Twitter</a></li>
                    <li><a href="#">Instagram</a></li>
                </ul>
            </div>

            <!-- Section: Make Money with Us -->
            <div>
                <h3>Make Money with Us</h3>
                <ul>
                    <li><a href="#">Sell on SportsFit</a></li>
                    <li><a href="#">Sell under SportsFit Accelerator</a></li>
                    <li><a href="#">Protect and Build Your Brand</a></li>
                    <li><a href="#">SportsFit Global Selling</a></li>
                    <li><a href="#">Supply to sportsFit</a></li>
                    <li><a href="#">Become an Affiliate</a></li>
                    <li><a href="#">Fulfilment by SportsFit</a></li>
                    <li><a href="#">Advertise Your Products</a></li>
                    <li><a href="#">SportsFit Pay on Merchants</a></li>
                </ul>
            </div>

            <!-- Section: Let Us Help You -->
            <div>
                <h3>Let Us Help You</h3>
                <ul>
                    <li><a href="#">Your Account</a></li>
                    <li><a href="#">Returns Centre</a></li>
                    <li><a href="#">Recalls and Product Safety Alerts</a></li>
                    <li><a href="#">100% Purchase Protection</a></li>
                    <li><a href="#">Help</a></li>
                </ul>
            </div>
        </div>
            <div class="footer-bottom">
             <p><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(245, 236, 236, 1);transform: ;msFilter:;"><path d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm7.931 9h-2.764a14.67 14.67 0 0 0-1.792-6.243A8.013 8.013 0 0 1 19.931 11zM12.53 4.027c1.035 1.364 2.427 3.78 2.627 6.973H9.03c.139-2.596.994-5.028 2.451-6.974.172-.01.344-.026.519-.026.179 0 .354.016.53.027zm-3.842.7C7.704 6.618 7.136 8.762 7.03 11H4.069a8.013 8.013 0 0 1 4.619-6.273zM4.069 13h2.974c.136 2.379.665 4.478 1.556 6.23A8.01 8.01 0 0 1 4.069 13zm7.381 6.973C10.049 18.275 9.222 15.896 9.041 13h6.113c-.208 2.773-1.117 5.196-2.603 6.972-.182.012-.364.028-.551.028-.186 0-.367-.016-.55-.027zm4.011-.772c.955-1.794 1.538-3.901 1.691-6.201h2.778a8.005 8.005 0 0 1-4.469 6.201z"></path></svg>English India</p>
            </div>
            <p>Your Support Our Efforts</p>
            <p>&copy; 2024 SportsFit. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """


if __name__ == "__main__":
    cherrypy.quickstart(Products(), '/products')

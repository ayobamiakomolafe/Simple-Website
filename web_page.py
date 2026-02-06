import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling to the Streamlit app"""
    st.markdown("""
    <style>
    /* Main title styling */
    h1 {
        text-align: center;
        color: #2c3e50;
        font-weight: 700;
        border-bottom: 4px solid #e74c3c;
        padding-bottom: 15px;
        margin-bottom: 25px;
    }
    
    /* Restaurant header styling */
    h2 {
        color: #e74c3c;
        font-weight: 600;
        border-left: 5px solid #e74c3c;
        padding-left: 15px;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    
    /* Introduction text styling */
    .intro-text {
        font-size: 16px;
        color: #34495e;
        line-height: 1.6;
        background-color: #ecf0f1;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 30px;
        border-left: 4px solid #e74c3c;
    }
    
    /* Address and rating styling */
    .info-box {
        background-color: #f8f9fa;
        border-radius: 6px;
        padding: 12px 15px;
        margin: 10px 0;
        border-left: 3px solid #3498db;
        font-weight: 500;
        color: #2c3e50;
    }
    
    .address-icon::before {
        content: "📍 ";
        margin-right: 5px;
    }
    
    .rating-icon::before {
        content: "⭐ ";
        margin-right: 5px;
    }
    
    /* Description text styling */
    .description {
        font-size: 15px;
        color: #555;
        line-height: 1.7;
        text-align: justify;
        margin: 20px 0;
        background-color: #fafafa;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #27ae60;
    }
    
    /* Image gallery styling */
    .gallery {
        margin: 20px 0;
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Container styling */
    .restaurant-container {
        background-color: white;
        border-radius: 10px;
        padding: 25px;
        margin: 30px 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        border-top: 4px solid #e74c3c;
    }
    
    /* Divider styling */
    hr {
        border: none;
        height: 3px;
        background: linear-gradient(to right, #e74c3c, #ecf0f1);
        margin: 40px 0;
    }
    
    /* Overall background */
    body {
        background-color: #f5f7fa;
    }
    
    </style>
    """, unsafe_allow_html=True)

def  main():

    import streamlit as st
    from PIL import Image
    import sys
    import os
    
    # Apply custom CSS
    apply_custom_css()
    
    st.title("TOP 20 RESTAURANTS IN SYDNEY")
    st.markdown("""<div class="intro-text">
    Have you ever wanted to grab great food and tried to search for the best local restaurants and food
    spots but you spend way more time reading reviews than actually getting a feed? Well,
    we have created a list of the best local Sydney food spots to save your time. Explore these 20 exceptional dining destinations across Sydney.
    </div>""", unsafe_allow_html=True)

    Quay=st.container()
    La_Salut=st.container()
    Lankan_Filling_Station =st.container()
    Cafe_Paci =st.container()
    Lolas_Level_1 =st.container()
    Saint_Peter =st.container()
    Ursulas_Paddington =st.container()
    Sixpenny =st.container()
    Ester =st.container()
    Sean=st.container()
    LuMi =st.container()
    Odd_Culture_Newtown =st.container()
    Bentley_Restaurant_and_Bar =st.container()
    Hubert =st.container()
    Margaret =st.container()
    Firedoor =st.container()
    Chaco_Bar =st.container()
    Automata =st.container()
    William_Street=st.container()
    Sang_by_Mabasa =st.container()



    names=["1.\xa0Quay",  "2.\xa0La Salut", "3. Lankan Filling Station" ,"4.\xa0Café Paci", "5.\xa0Lola's Level 1", "6.\xa0Saint Peter","7.\xa0Ursula's Paddington", "8.\xa0Sixpenny","9.\xa0Ester",
           "10.\xa0Sean's","11.\xa0LuMi","12.\xa0Odd Culture Newtown", "13.\xa0Bentley Restaurant and Bar","14.\xa0Hubert", "15.\xa0Margaret","16.\xa0Firedoor",
           "17.\xa0Chaco Bar","18.\xa0Automata", "19.\xa010 William Street","20.\xa0Sáng by Mabasa"]

    names = [os.path.join("Scrapped_Contents", name) for name in names]
    
    website= [
    """If you’re seeking a fine dining experience that captures the essence of Sydney’s natural beauty, this restaurant stands out as an exceptional choice. Set against the breathtaking backdrop of Sydney Harbour, it offers sweeping panoramic views of the water, the iconic skyline, and the ever-changing light that dances across the bay. The setting alone is enough to make any meal feel special, but the culinary experience elevates it even further. Led by acclaimed Australian chef Peter Gilmore, the menu showcases modern Australian cuisine at its most innovative. Gilmore is known for his meticulous attention to detail, his deep respect for seasonal produce, and his ability to transform familiar ingredients into something extraordinary. Each dish is crafted with precision, creativity, and a sense of playfulness that keeps diners engaged from the first bite to the last. Expect beautifully plated dishes that balance texture, flavour, and technique in surprising ways. The menu often features native Australian ingredients, sustainably sourced seafood, and vegetables grown specifically for the restaurant’s kitchen. The wine list is equally impressive, offering both local and international selections that pair seamlessly with the food. Whether you’re celebrating a special occasion or simply indulging in a memorable night out, this restaurant delivers an experience that feels both luxurious and deeply connected to its surroundings. The combination of world-class cuisine, attentive service, and stunning harbour views makes it one of Sydney’s most iconic dining destinations.""",

    """Inspired by the vibrant culinary traditions of Barcelona, this Redfern gem brings the spirit of Spain to Sydney with remarkable authenticity and flair. The restaurant is guided by chef Scott McComas-Williams, whose passion for Spanish cuisine shines through in every dish. His menu pays homage to the flavours of Catalonia and the broader Mediterranean, while celebrating the exceptional quality of Australian produce. The result is a dining experience that feels both transportive and grounded in local identity. Expect bold flavours, thoughtful techniques, and a sense of conviviality that mirrors the lively tapas bars of Barcelona. The menu often features charcuterie, seafood, grilled meats, and vegetable-forward dishes that highlight the region’s culinary diversity. Each plate is designed for sharing, encouraging a communal dining style that sparks conversation and connection. The atmosphere is warm, energetic, and stylish without feeling pretentious. Mediterranean influences extend beyond the food, with a wine list that includes Spanish varietals alongside Australian interpretations of classic European styles. Whether you’re enjoying a long lunch with friends or a cosy dinner for two, the restaurant offers a sensory journey through Spain’s coastal flavours and rustic traditions. It’s a place where the richness of Spanish cuisine meets the freshness of Australian ingredients, resulting in a memorable and delicious fusion that keeps diners returning again and again.""",

    """This casual eatery offers a vibrant and heartfelt celebration of Sri Lankan cuisine, reimagined through the lens of contemporary Australian dining. Led by chef and owner O Tama Carey, the restaurant brings together traditional Sri Lankan flavours with modern sensibilities, creating dishes that feel both comforting and refreshingly new. The atmosphere is relaxed and welcoming, making it an ideal spot for diners who want to explore bold, aromatic flavours without the formality of fine dining. The menu features an array of Sri Lankan staples—think hoppers (delicate bowl-shaped pancakes), fragrant curries, sambols, and spiced vegetable dishes—each prepared with care and respect for their cultural origins. Carey’s approach highlights the complexity of Sri Lankan cuisine, from its use of toasted spices to its balance of heat, acidity, and richness. The dishes are vibrant in both colour and flavour, offering a sensory experience that is deeply satisfying. Drinks often include creative takes on traditional beverages, such as spiced teas or cocktails infused with tropical ingredients. The restaurant’s easygoing ambience encourages diners to linger, share plates, and enjoy the lively interplay of flavours. It’s a place where tradition meets innovation, resulting in a dining experience that feels authentic yet contemporary. Whether you’re familiar with Sri Lankan cuisine or discovering it for the first time, this restaurant offers a delicious and memorable introduction to its culinary heritage.""",

    """This hip, industrial-chic restaurant offers a unique fusion of flavours shaped by the diverse culinary background of Finnish-born chef Pasi Petanen. Known for his inventive approach to Modern Australian cuisine, Petanen draws inspiration from his Nordic roots while incorporating influences from Mexican and Vietnamese cooking. The result is a menu that feels adventurous, unexpected, and deeply satisfying. The restaurant’s interior reflects its creative spirit, featuring raw concrete, exposed beams, and minimalist design elements that create a stylish yet unpretentious atmosphere. The open kitchen allows diners to witness the artistry behind each dish, adding a sense of theatre to the experience. Petanen’s menu changes frequently to reflect seasonal availability, but diners can expect bold flavour combinations, playful textures, and a thoughtful balance of comfort and innovation. Dishes may incorporate fermented elements, smoked ingredients, or spice-forward components that nod to global culinary traditions. Despite the eclectic influences, the menu remains cohesive, unified by Petanen’s precise technique and imaginative vision. The restaurant also offers a curated selection of wines and cocktails that complement the food’s complexity. Whether you’re a seasoned foodie or simply curious about new flavour experiences, this restaurant delivers a dining journey that feels both familiar and refreshingly original. It’s a standout destination for those who appreciate creativity, craftsmanship, and a touch of culinary rebellion.""",

    """This South European-inspired restaurant embraces the joy of shared dining with a menu that celebrates the flavours of Italy, Spain, Greece, and the Mediterranean coast. The philosophy here is simple: food should be free-spirited, generous, and full of life. The dishes are designed for sharing, encouraging a communal dining experience that mirrors the warm hospitality of Southern Europe. Expect vibrant salads, rustic pastas, grilled meats, fresh seafood, and vegetable-forward plates that highlight the region’s sun-soaked ingredients. The kitchen takes a contemporary approach to presentation, elevating traditional flavours with modern techniques and artistic plating. The atmosphere is lively and inviting, with a stylish interior that blends Mediterranean charm with contemporary design. Whether you’re enjoying a leisurely lunch or a festive dinner with friends, the restaurant offers a sense of escape—a momentary journey to the shores of the Mediterranean. The wine list features a thoughtful selection of European varietals alongside Australian wines that pair beautifully with the menu’s bold, fresh flavours. Desserts often draw inspiration from classic Mediterranean sweets, offering a sweet finish that feels both nostalgic and refined. This restaurant is perfect for diners who crave generous portions, vibrant flavours, and a dining experience that feels celebratory from start to finish.""",

    """This highly acclaimed seafood restaurant is a must-visit for anyone passionate about fresh, innovative ocean-to-table dining. Led by chef Josh Niland, the restaurant has earned international recognition for its groundbreaking approach to seafood preparation—particularly its pioneering use of dry-aged fish. Niland’s philosophy centres on sustainability, respect for the whole fish, and a commitment to reducing waste. His techniques transform seafood into something extraordinary, revealing flavours and textures that many diners have never experienced before. The menu changes frequently based on the day’s catch, ensuring that every dish is as fresh and seasonal as possible. Diners can expect a mix of raw, grilled, roasted, and dry-aged preparations, each showcasing Niland’s exceptional skill and creativity. One of the highlights of the dining experience is the open kitchen, where guests can watch the chef at work. This intimate, behind-the-scenes view adds a sense of connection and appreciation for the craftsmanship involved. The restaurant’s atmosphere is refined yet approachable, with a focus on letting the food speak for itself. The wine list is carefully curated to complement the delicate flavours of the seafood, offering both local and international selections. Whether you’re a seafood enthusiast or simply curious about Niland’s innovative techniques, this restaurant promises a memorable and eye-opening culinary experience.""",

    """At his first solo restaurant, acclaimed chef Phil Wood presents a thoughtful and deeply personal exploration of Australian cuisine. His menu is driven by a commitment to exceptional produce, classic European techniques, and a desire to expand the boundaries of what Australian food can be. Wood’s cooking is elegant, refined, and grounded in a deep respect for local ingredients. Each dish is crafted with precision, showcasing the natural beauty and flavour of the produce while incorporating subtle influences from global culinary traditions. The restaurant’s atmosphere is warm and sophisticated, making it an ideal setting for both intimate dinners and celebratory gatherings. Private dining options are available for special occasions, offering a more exclusive experience for guests who want to enjoy Wood’s cuisine in a more intimate setting. The menu often features seasonal vegetables, sustainably sourced meats, and seafood prepared with meticulous attention to detail. Desserts are equally thoughtful, balancing sweetness with complexity. The wine list highlights Australian producers alongside international favourites, ensuring a perfect pairing for every course. This restaurant is a testament to Wood’s culinary vision—a place where tradition meets innovation, and where diners can experience the richness and diversity of Australian cuisine in a refined and welcoming environment.""",

    """Chefs Daniel Puskas and Anthony Schifilliti lead this cosy, modern Australian restaurant with a shared passion for storytelling through food. Their philosophy centres on celebrating the people, landscapes, and ingredients that define Australia. By working closely with local growers, producers, and suppliers, they create a menu that reflects the country’s diverse culinary identity. Each dish is crafted with precision and intention, highlighting the natural flavours of the ingredients while incorporating creative techniques that elevate the dining experience. The restaurant’s intimate setting fosters a sense of warmth and connection, making it an ideal spot for diners who appreciate thoughtful, ingredient-driven cuisine. The menu changes regularly to reflect seasonal availability, ensuring that every visit offers something new and exciting. Expect beautifully plated dishes that balance texture, flavour, and visual appeal. The wine list features a curated selection of Australian varietals, chosen to complement the menu’s evolving flavours. The restaurant’s commitment to sustainability and local sourcing is evident in every aspect of the dining experience, from the ingredients to the service. It’s a place where passion, precision, and creativity come together to tell a uniquely Australian story—one plate at a time.""",

    """This trendy restaurant blends industrial aesthetics with the warmth of a wood-fired kitchen, creating a dining experience that feels both modern and inviting. Known for its eclectic approach to Modern Australian cuisine, the restaurant embraces farm-to-table principles, transforming high-quality local ingredients into innovative, flavour-forward dishes. The concrete-walled space is softened by the glow of the wood-fired oven, which serves as both a visual centrepiece and a key element of the cooking process. The menu often features charred vegetables, smoky meats, and rustic breads, all infused with the distinctive flavours of open-fire cooking. The chefs take inspiration from global culinary traditions while maintaining a strong connection to Australian produce. The result is a menu that feels adventurous yet grounded, offering something for both curious diners and those seeking comfort in familiar flavours. The atmosphere is lively and contemporary, making it a popular spot for both casual dinners and special nights out. The wine list includes a mix of natural wines, local favourites, and international selections that pair beautifully with the smoky, earthy flavours of the food. Whether you’re drawn by the ambience, the innovative menu, or the theatrical cooking style, this restaurant delivers a memorable dining experience that lingers long after the meal ends.""",

    """Affectionately known as Sean’s since its opening in 1993, this charming seaside restaurant has become a beloved institution for locals and visitors alike. Nestled along the coastline, it offers stunning surf views that create a serene and picturesque backdrop for every meal. The restaurant embraces a market-driven philosophy, with a menu that changes daily based on the freshest available ingredients. This approach ensures that each dish feels vibrant, seasonal, and deeply connected to the surrounding environment. The food is comforting yet refined, blending home-style cooking with modern culinary sensibilities. Expect hearty plates, fresh seafood, vibrant salads, and rustic desserts that evoke a sense of nostalgia. The atmosphere is relaxed and intimate, with a small dining room that feels warm and welcoming. Outdoor seating allows guests to enjoy the ocean breeze and panoramic views, making it an ideal spot for leisurely lunches or romantic dinners. Despite its reputation and longevity, the restaurant remains surprisingly affordable, offering exceptional value without compromising on quality. The wine list is thoughtfully curated to complement the menu’s evolving flavours. Whether you’re a longtime fan or a first-time visitor, Sean’s offers a dining experience that feels both timeless and deeply personal—a true coastal gem.""",

    """LuMi is an intimate fine-dining destination that blends Asian-inspired flavours with refined European techniques, resulting in a progressive tasting menu that feels both sophisticated and imaginative. The restaurant’s minimalist design creates a serene and elegant atmosphere, allowing the food to take centre stage. Each course is meticulously crafted, showcasing bold flavours, delicate textures, and artistic presentation. The chefs draw inspiration from Japanese, Italian, and broader Asian cuisines, creating a fusion that feels harmonious rather than forced. Expect dishes that balance umami, acidity, sweetness, and freshness in surprising and delightful ways. The tasting menu evolves with the seasons, ensuring that each visit offers a new culinary journey. Service is highly personalized, with staff guiding diners through each course and offering thoughtful wine pairings that enhance the experience. The restaurant’s intimate size adds to its exclusivity, making it a popular choice for special occasions and memorable nights out. LuMi’s commitment to creativity, precision, and flavour has earned it a reputation as one of Sydney’s most exciting fine-dining venues. It’s a place where culinary artistry meets warm hospitality, resulting in an unforgettable dining experience that lingers long after the final course.""",

    """Located in the vibrant heart of Newtown, Odd Culture brings a fresh and experimental approach to contemporary dining. The restaurant is known for its creative small plates, innovative flavour combinations, and a curated selection of natural wines that reflect its adventurous spirit. The atmosphere is eclectic and energetic, mirroring the neighbourhood’s artistic and alternative vibe. The menu changes frequently, driven by seasonal produce and the chefs’ desire to push culinary boundaries. Expect dishes that play with texture, acidity, fermentation, and unexpected pairings. The result is a dining experience that feels dynamic, surprising, and deeply satisfying. The wine list is a standout feature, showcasing unique varietals and minimal-intervention wines that complement the bold flavours of the food. The restaurant encourages exploration, inviting diners to try new combinations and discover flavours they may not have encountered before. The interior blends rustic elements with modern design, creating a space that feels both stylish and relaxed. Whether you’re a wine enthusiast, a food lover, or simply someone seeking something different, Odd Culture offers a memorable and exciting dining experience that captures the creative spirit of Newtown.""",

    """Bentley Restaurant and Bar is an elegant and sophisticated dining destination that combines contemporary Australian cuisine with impeccable service and a refined atmosphere. The restaurant is known for its innovative menu, which features premium ingredients prepared with precision and artistry. Each dish is thoughtfully composed, balancing flavour, texture, and visual appeal. The chefs draw inspiration from global culinary traditions while maintaining a strong focus on Australian produce. The result is a menu that feels modern, dynamic, and deeply satisfying. The restaurant’s interior is sleek and stylish, with a design that enhances the sense of luxury without feeling overly formal. The bar is a highlight, offering expertly crafted cocktails and an extensive wine list that includes both local and international selections. The wine program is particularly impressive, featuring rare bottles and thoughtful pairings that elevate the dining experience. Bentley is an ideal choice for special occasions, business dinners, or any moment that calls for a touch of sophistication. The combination of exceptional food, attentive service, and a polished atmosphere makes it one of Sydney’s premier dining destinations.""",

    """Hubert is a French-inspired brasserie that exudes Parisian charm and old-world elegance. From the moment you step inside, you’re transported to a bygone era of candlelit dining rooms, vintage décor, and warm, attentive service. The restaurant celebrates classic French cuisine, prepared with time-honoured techniques and a deep respect for tradition. Expect rich sauces, perfectly cooked meats, delicate seafood dishes, and indulgent desserts that capture the essence of European dining. The menu is both nostalgic and refined, offering comfort and sophistication in equal measure. The wine list is extensive, featuring French varietals alongside carefully selected international bottles. The atmosphere is intimate and romantic, making it a popular choice for date nights, celebrations, and memorable evenings out. Live music and a lively bar add to the restaurant’s charm, creating an ambience that feels both timeless and vibrant. Hubert is more than just a meal—it’s an experience that celebrates the beauty of classic French hospitality and culinary craftsmanship.""",

    """Margaret offers a sophisticated yet welcoming dining experience that highlights the best of modern Australian cuisine. The restaurant is committed to using seasonal, locally sourced ingredients, ensuring that each dish reflects the richness and diversity of Australia’s culinary landscape. The menu blends contemporary techniques with global influences, resulting in dishes that are both familiar and exciting. Expect beautifully plated plates that showcase fresh seafood, vibrant vegetables, and premium meats prepared with precision. The interior is stylish and inviting, with warm lighting and thoughtful design elements that create a comfortable and elegant atmosphere. The staff are attentive and knowledgeable, offering personalized recommendations and ensuring that every guest feels well cared for. The wine list features a curated selection of Australian and international bottles that pair seamlessly with the menu. Whether you’re celebrating a special occasion or simply enjoying a night out, Margaret delivers a memorable dining experience that combines exceptional food, warm hospitality, and a refined yet relaxed ambience.""",

    """Firedoor is a one-of-a-kind dining destination dedicated to the primal art of cooking with fire. The restaurant features an open kitchen where flames, embers, and smoke play a central role in the preparation of every dish. This theatrical setup allows diners to witness the skill and precision required to cook over wood fire, creating a sense of excitement and anticipation. The menu is driven by seasonal ingredients, with each dish showcasing the unique flavours that only fire can impart. Expect smoky vegetables, perfectly charred meats, and seafood cooked with incredible finesse. The chefs use different types of wood to achieve specific flavours, adding depth and complexity to the dishes. The atmosphere is warm and rustic, with an industrial edge that complements the dramatic cooking style. The wine list is carefully curated to match the bold, smoky flavours of the food. Firedoor offers a dining experience that feels both primal and sophisticated—a celebration of craftsmanship, flavour, and the elemental beauty of fire.""",

    """Chaco Bar brings the vibrant flavours of South America to Sydney, offering a lively and energetic dining experience centred around grilled meats and fresh, bold ingredients. The restaurant embraces the spirit of Latin cuisine, with a menu that features generous portions, smoky flavours, and dishes designed for sharing. Expect perfectly grilled steaks, flavourful skewers, zesty salads, and hearty sides that highlight the region’s culinary diversity. The atmosphere is upbeat and festive, making it an ideal spot for group gatherings, celebrations, or casual nights out. The staff are friendly and enthusiastic, adding to the restaurant’s welcoming vibe. Drinks often include Latin-inspired cocktails, refreshing beers, and wines that pair beautifully with the robust flavours of the food. Chaco Bar is a place where diners can enjoy the warmth and vibrancy of South American hospitality, brought to life through delicious food, lively ambience, and a commitment to authenticity.""",
      
    """Automata is a cutting-edge restaurant where technology meets culinary artistry, offering one of Sydney’s most forward-thinking dining experiences. The concept revolves around a hybrid kitchen that seamlessly blends traditional craftsmanship with modern innovation, resulting in dishes that feel both familiar and futuristic. The restaurant’s sleek, industrial-inspired interior sets the tone for a meal that is as visually striking as it is intellectually engaging. Every plate is designed with intention, showcasing bold flavours, unexpected textures, and meticulous technique. Automata’s tasting menus evolve frequently, reflecting seasonal produce and the creative impulses of the culinary team. Diners can expect a journey through layered flavours, from delicate seafood preparations to robust meat dishes and inventive vegetable courses. The restaurant’s commitment to pushing boundaries is evident not only in the food but also in the beverage program, which features a curated selection of wines, sake, and non-alcoholic pairings that complement the menu’s complexity. Service is polished yet relaxed, creating an atmosphere where guests can fully immerse themselves in the experience without feeling overwhelmed. Automata represents the future of fine dining in Sydney—an intersection of creativity, precision, and innovation that leaves a lasting impression long after the final course.""",

    """10 William Street offers a refined yet approachable contemporary Australian dining experience in a sophisticated, intimate setting. Known for its commitment to premium local ingredients, the restaurant crafts dishes that highlight the beauty of seasonal produce while embracing a modern culinary sensibility. The menu is concise but thoughtful, with each plate showcasing a balance of flavour, texture, and technique. From handmade pastas to vibrant vegetable dishes and expertly prepared proteins, the food reflects a deep respect for quality ingredients and a dedication to craftsmanship. The atmosphere is warm and stylish, making it an ideal venue for business dinners, romantic evenings, or celebratory gatherings. One of the standout features of 10 William Street is its exceptional wine list, curated with care to include both Australian favourites and unique international selections. The knowledgeable staff are adept at guiding guests through pairings that elevate the dining experience. The restaurant’s understated elegance, combined with its focus on thoughtful cooking and professional service, has earned it a reputation as one of Sydney’s most reliable and beloved dining destinations. It’s a place where simplicity meets sophistication, offering a memorable meal without unnecessary pretension.""",

    """Sang by Mabasa brings the rich culinary traditions of Vietnam to Sydney, offering an elevated dining experience that honours authenticity while embracing contemporary refinement. The restaurant is known for its meticulous attention to detail, from the selection of premium ingredients to the precise execution of each dish. Traditional Vietnamese flavours—bright herbs, aromatic broths, delicate spices—are presented with a modern sensibility that enhances their depth and complexity. The menu features a thoughtful mix of classic dishes and innovative interpretations, showcasing the diversity of Vietnamese cuisine. Expect beautifully crafted plates that highlight fresh seafood, tender meats, and vibrant vegetables, all prepared with balance and harmony in mind. The elegant interior design creates a serene and sophisticated atmosphere, making Sang by Mabasa an ideal destination for special occasions or intimate dinners. Service is attentive and knowledgeable, reflecting the restaurant’s commitment to hospitality and cultural respect. Every element of the experience—from the food to the ambience—celebrates the richness of Southeast Asian cuisine at its finest. Sang by Mabasa stands as a testament to how traditional flavours can be elevated through modern technique without losing their soul."""
]

    
    address=[
        ' Upper Level Overseas Passenger Terminal, The Rocks',
        ' 305 Cleveland St, Redfern',
        ' Ground Floor, 58 Riley St, Darlinghurst',
        ' 131 King Street, Newtown',
        ' Level 1/180-186 Campbell Parade, Bondi Beach',
        ' 362 Oxford St, Paddington',
        ' 92 Hargraves St, Paddington',
        ' 83 Percival Rd, Stanmore',
        ' 46-52 Meagher St, Chippendale',
        ' 270 Campbell Parade, North Bondi',
        ' Unit 3, 80 Bourke Rd, Alexandria',
        ' 72a King Street, Newtown',
        ' 4 Martin Place, Sydney CBD',
        ' 61 Riley Street, Darlinghurst',
        ' 335 Crown Street, Surry Hills',
        ' Level 2, 68 Ebley Street, Bondi',
        ' 16 Young Street, Waterloo',
        ' 45 Charlotte Lane, Sydney CBD',
        ' 10 William Street, East Sydney',
        ' 197 Pitt Street, Sydney CBD'
    ]
    
    rating=[
        '4.5 stars',
        '4.7 stars',
        '4.2 stars',
        '4.7 stars',
        '3.6 stars',
        '4.6 stars',
        '4.5 stars',
        '4.8 stars',
        '4.5 stars',
        '4.1 stars',
        '4.6 stars',
        '4.3 stars',
        '4.4 stars',
        '4.5 stars',
        '4.2 stars',
        '4.7 stars',
        '4.0 stars',
        '4.6 stars',
        '4.3 stars',
        '4.4 stars'
    ]

    # Restaurant display function
    def display_restaurant(container, name_idx):
        with container:
            st.markdown("""<div class="restaurant-container">""", unsafe_allow_html=True)
            st.header(os.path.basename(names[name_idx]))
            st.markdown(f"""<div class="info-box address-icon">Address: {address[name_idx]}</div>""", unsafe_allow_html=True)
            st.markdown(f"""<div class="info-box rating-icon">Rating: {rating[name_idx]}</div>""", unsafe_allow_html=True)
            
            # Display images
            col1, col2, col3, col4, col5 = st.columns(5)
            try:
                img = Image.open(names[name_idx] + '1.JPG')
                col1.image(img, width='stretch')
            except:
                pass
            try:
                img = Image.open(names[name_idx] + '2.JPG')
                col2.image(img, width='stretch')
            except:
                pass
            try:
                img = Image.open(names[name_idx] + '3.JPG')
                col3.image(img, width='stretch')
            except:
                pass
            try:
                img = Image.open(names[name_idx] + '4.JPG')
                col4.image(img, width='stretch')
            except:
                pass
            try:
                img = Image.open(names[name_idx] + '5.JPG')
                col5.image(img, width='stretch')
            except:
                pass
            
            st.markdown(f"""<div class="description">{website[name_idx]}</div>""", unsafe_allow_html=True)
            st.markdown("""</div>""", unsafe_allow_html=True)

    # Display all restaurants
    display_restaurant(Quay, 0)
    display_restaurant(La_Salut, 1)
    display_restaurant(Lankan_Filling_Station, 2)
    display_restaurant(Cafe_Paci, 3)
    display_restaurant(Lolas_Level_1, 4)
    display_restaurant(Saint_Peter, 5)
    display_restaurant(Ursulas_Paddington, 6)
    display_restaurant(Sixpenny, 7)
    display_restaurant(Ester, 8)
    display_restaurant(Sean, 9)
    display_restaurant(LuMi, 10)
    display_restaurant(Odd_Culture_Newtown, 11)
    display_restaurant(Bentley_Restaurant_and_Bar, 12)
    display_restaurant(Hubert, 13)
    display_restaurant(Margaret, 14)
    display_restaurant(Firedoor, 15)
    display_restaurant(Chaco_Bar, 16)
    display_restaurant(Automata, 17)
    display_restaurant(William_Street, 18)
    display_restaurant(Sang_by_Mabasa, 19)

if __name__ == '__main__':
    main()

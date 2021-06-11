import streamlit as st

def info(label):
    
    if label=='Quartz':
        info_kuvars = ''.join("Quartz is a chemical compound consisting of one part silicon and two parts oxygen."
                       " It is silicon dioxide (SiO2). It is the most abundant mineral found at Earth's surface,"
                       " and its unique properties make it one of the most useful natural substances."
                       "Quartz is the most abundant and widely distributed mineral found at Earth's surface."
                       " It is present and plentiful in all parts of the world. It forms at all temperatures."
                       "It is abundant in igneous, metamorphic, and sedimentary rocks."
                       " It is highly resistant to both mechanical and chemical weathering. "
                       "This durability makes it the dominant mineral of mountaintops and the primary constituent of beach, river, and desert sand. "
                       "Quartz is ubiquitous, plentiful and durable. Minable deposits are found throughout the world.")
      
        return (st.header(info_kuvars))
    
    elif label=='Pyrite':
        info_pirit = ''.join("Pyrite is a brass-yellow mineral with a bright metallic luster."
                      "It has a chemical composition of iron sulfide (FeS2) and is the most common sulfide mineral."
                      "It forms at high and low temperatures and occurs, usually in small quantities, in igneous, metamorphic, and sedimentary rocks worldwide."
                      "Pyrite is so common that many geologists would consider it to be a ubiquitous mineral."
                      "The name 'pyrite' is after the Greek 'pyr' meaning 'fire.' "
                      "This name was given because pyrite can be used to create the sparks needed for starting"
                      "a fire if it is struck against metal or another hard material. Pieces of pyrite have also been used as a spark-producing material in flintlock firearms."
                      "Pyrite has a nickname that has become famous - 'Fool's Gold.'"
                      "The mineral's gold color, metallic luster, and high specific gravity often cause it to be mistaken for gold by inexperienced prospectors." 
                      "However, pyrite is often associated with gold. The two minerals often form together, and in some deposits pyrite contains enough included gold to warrant mining.")
        
        return (st.header(info_pirit))
    
    elif label=='Amethyst':
        info_ametist = ''.join("Amethyst is a well known mineral and gemstone."
                      "It is the purple variety of the mineral Quartz, and its most valuable and prized variety."
                      "Its name derives from the Greek 'amethystos', which means 'not drunken',"
                      "as Amethyst in antiquity was thought to ward off drunkenness."
                      "The color of some Amethyst specimens from certain localities slowly fade upon prolonged exposure to light."
                      "When used as a gemstone, Amethyst is often heat treated to deepen the color,"
                      "or to transform it into Citrine. Some varieties may also change to a light green color, which is given the trade name "
                      "'Prasiolite', or 'Green Amethyst', as it is more commonly known in the gem trade."
                      "Amethyst is most prevalent as small stubby pyramidal crystals, although several localities "
                      "such as the Mexican occurrences are well-known for producing elegantly tall prismatic crystals, "
                      "which are very highly regarded by collectors. Amethyst also forms the internal lining of geodes, "
                      "some of which can be over 10 feet tall and weighing several tons.")
        
        return (st.header(info_ametist))
   
    elif label=='Boron':
        info_bor =''.join("Boron minerals are natural compounds containing boron oxide in different proportions."
                    "There are 230 different boron minerals in the nature."
                    "The most important boron minerals in commercial terms are;"
                    "Tincal, Colemanite, Kernite, Ulexite, Pandermite, Boracite, Szaybelite and Hydroboracite."
                    "The main boron minerals transformed by Eti Maden, the World Boron Leader, "
                    "into high value added products in international quality standards are; Tincal, Colemanite and Ulexite.")
        
        return (st.header(info_bor))
    
    elif label=='Galena':
        info_galen = ''.join("Galena is a lead sulfide mineral with a chemical composition of PbS."
                      "It is the world's primary ore of lead and is mined from a large number of deposits"
                      "in many countries. It is found in igneous and metamorphic rocks in medium- to"
                      "low-temperature hydrothermal veins. In sedimentary rocks it occurs as veins, "
                      "breccia cements, isolated grains, and as replacements of limestone and dolostone."
                      "Galena is very easy to identify."
                      "Freshly broken pieces exhibit perfect cleavage in three directions that intersect at 90 degrees."
                      "It has a distinct silver color and a bright metallic luster."
                      "Galena tarnishes to a dull gray. Because lead is a primary element in galena,"
                      "the mineral has a high specific gravity (7.4 to 7.6) that is immediately noticed when picking up even small pieces. "
                      "Galena is soft with a Mohs hardness of 2.5+ and produces a gray to black streak."
                      "Crystals are common and they usually are cubes, octahedrons, or modifications.")
        
        return (st.header(info_galen))
    
    elif label=='Malachite':
        info_malakit = ''.join("Malachite is a green copper carbonate hydroxide mineral with a chemical composition"
                        "of Cu2(CO3)(OH)2. It was one of the first ores used to produce copper metal."
                        "It is of minor importance today as an ore of copper because it is usually found "
                        "in small quantities and can be sold for higher prices for other types of use."
                        "Malachite has been used as a gemstone and sculptural material for thousands of years"
                        "and is still popular today. Today it is most often cut into cabochons or beads for jewelry use."
                        "Malachite has a green color that does not fade over time or when exposed to light."
                        "Those properties, along with its ability to be easily ground to a powder,"
                        "made malachite a preferred pigment and coloring agent for thousands of years.")
        
        return (st.header(info_malakit))
    
    elif label=='Halite':
        info_halit = ''.join("Halite is the mineral name for the substance that everyone knows as 'salt.'"
                              "Its chemical name is sodium chloride, and a rock composed primarily of halite"
                              "is known as 'rock salt.'"
                              "Halite is mainly a sedimentary mineral that usually forms in arid climates"
                              "where ocean water evaporates. However, many inland lakes such as the Great Salt"
                              "Lake of North America and the Dead Sea between Jordan and Israel are also locations"
                              "where halite is forming today. Over geologic time, several enormous salt deposits"
                              "have been formed when repeated episodes of seawater evaporation occurred in restricted basins."
                              "Some of these deposits are thousands of feet thick. When buried deeply they can erupt to form salt domes.")    
        return st.header(info_halit)
    
    elif label=='Chalcopyrite':
        info_kalkopirit = ''.join("Chalcopyrite is a brass-yellow mineral with a chemical composition of CuFeS2."
                                  "It occurs in most sulfide mineral deposits throughout the world and has been"
                                  "the most important ore of copper for thousands of years."
                                  "The surface of chalcopyrite loses its metallic luster and brass-yellow"
                                  "color upon weathering. It tarnishes to a dull, gray-green color, but in"
                                  "the presence of acids the tarnish can develop a red to blue to purple"
                                  "iridescence.The iridescent colors of weathered chalcopyrite attract"
                                  "attention. Some souvenir shops sell chalcopyrite that has been treated"
                                  "with acid as 'peacock ore.' But, 'peacock ore' is a more appropriate"
                                  "name for the mineral bornite.")    
        return st.header(info_kalkopirit)
    
    elif label=='Chromite':
        info_kromit = ''.join("Chromite is an oxide mineral composed of chromium, iron, and oxygen (FeCr2O4)."
                              "It is dark gray to black in color with a metallic to submetallic luster and a"
                              "high specific gravity. It occurs in basic and ultrabasic igneous rocks and in the metamorphic"
                              "and sedimentary rocks that are produced when chromite-bearing rocks are altered by heat or weathering." 
                              "Chromite is important because it is the only economic ore of chromium,"
                              " an essential element for a wide variety of metal, chemical, and manufactured"
                              " products. Many other minerals contain chromium, but none of them are found"
                              " in deposits that can be economically mined to produce chromium.")
        return st.header(info_kromit)
    
    elif label=='Obsidian':
        info_obsidyen = ''.join("Obsidian is an igneous rock that forms when molten rock material cools"
                                "so rapidly that atoms are unable to arrange themselves into a crystalline"
                                "structure. It is an amorphous material known as a 'mineraloid.'"
                                "The result is a volcanic glass with a smooth uniform texture that "
                                "breaks with a conchoidal fracture (see photo)."
                                "Obsidian is usually an extrusive rock - one that solidifies above Earth's"
                                "surface. However, it can form in a variety of cooling environments:"
                                "along the edges of a lava flow (extrusive)"
                                "along the edges of a volcanic dome (extrusive)"
                                "around the edges of a sill or a dike (intrusive)"
                                "where lava contacts water (extrusive)"
                                "where lava cools while airborne (extrusive)")
        return st.header(info_obsidyen)


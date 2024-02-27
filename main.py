if __name__ == '__main__':
    import streamlit as st
    st.title(":red[For Shariya with love]  :love_letter:",)
    st.write(":blue[Ingredients  by Dish]")
    round_digits = 3
    # Enter the number of Chicken Gyros
    chicken_gyro_num = st.number_input("Gyros :poultry_leg:", value=5, placeholder="Type a number...")
    st.write(":blue[Choose Chicken or Paneer:]")
    st.write("Chicken: ", round(.12*chicken_gyro_num,round_digits), "Kg  ----------------- Paneer: ", round(.075 * chicken_gyro_num, round_digits), " Kg")

    # Calculate each ingredient in terms of that
    chicken_gyro_ingredients_info = {"Maida" : {"Quantity" : round(.1*chicken_gyro_num,round_digits),
                                                "Units" : "Kg"},
                                     "Mayo - (in Chicken)" : {"Quantity" : round(7.2*chicken_gyro_num,round_digits),
                                                              "Units" : "Grams"},
                                     "Mayo - (in White Sauce)" : {"Quantity" : round(31*chicken_gyro_num,round_digits),
                                                                  "Units" : "Grams"},
                                     "Curd - (in White Sauce)" : {"Quantity" : round(9.3*chicken_gyro_num, round_digits),
                                                                  "Units" : "Grams"},
                                     "Vinegar - (in White Sauce)" : {"Quantity" : round(4*chicken_gyro_num,round_digits),
                                                                  "Units" : "Grams"},
                                     "Garlic (in White Source)": {"Quantity": round(.5 * chicken_gyro_num, round_digits),
                                                                    "Units": "Grams"},
                                     "Salad": {"Quantity": round(40 * chicken_gyro_num, round_digits),
                                                                    "Units": "Grams"},
                                     "Cumin": {"Quantity": round(.96 * chicken_gyro_num, round_digits),
                                                                    "Units": "Grams"},
                                     "Garlic (in Chicken": {"Quantity": round(4.2 * chicken_gyro_num, round_digits),
                                                                    "Units": "Grams"},
                                     }
    for ingredient, info_dict in chicken_gyro_ingredients_info.items():
        st.write(ingredient, " : ", info_dict["Quantity"], " ", info_dict["Units"])

    st.write("-------------------------------------------------------------------------------------")
    # Enter the number of Chicken Rice Platters
    chicken_rice_num = st.number_input("Rice Platters :rice:", value=5, placeholder="Type a number...")
    st.write(":blue[Choose Chicken or Paneer: ]")
    st.write("Chicken: ", round(.2*chicken_rice_num,round_digits), "Kg  ----------------- Paneer: ", round(.2*chicken_rice_num, round_digits), " Kg")

    # Calculate each ingredient in terms of that
    chicken_rice_ingredients_info = {"Rice" : {"Quantity" : round(.06*chicken_rice_num,round_digits),
                                                  "Units" : "Kg"},
                                     "Mayo - (in Chicken)" : {"Quantity" : round(12*chicken_rice_num,round_digits),
                                                              "Units" : "Grams"},
                                     "Mayo - (in White Sauce)" : {"Quantity" : round(33*chicken_rice_num,round_digits),
                                                                  "Units" : "Grams"},
                                     "Curd - (in White Sauce)" : {"Quantity" : round(9.3*chicken_rice_num, round_digits),
                                                                  "Units" : "Grams"},
                                     "Vinegar - (in White Sauce)" : {"Quantity" : round(4*chicken_rice_num,round_digits),
                                                                  "Units" : "Grams"},
                                     "Garlic (in White Source)": {"Quantity": round(.5 * chicken_rice_num, round_digits),
                                                                    "Units": "Grams"},
                                     "Salad": {"Quantity": round(40 * chicken_rice_num, round_digits),
                                                                    "Units": "Grams"},
                                     "Cumin - (in Chicken)": {"Quantity": round(1.2 * chicken_rice_num, round_digits),
                                                                    "Units": "Grams"},
                                     "Cumin - (in Rice)": {"Quantity": round(.4 * chicken_rice_num, round_digits),
                                                                    "Units": "Grams"},
                                     "Garlic (in Chicken)": {"Quantity": round(4.2 * chicken_rice_num, round_digits),
                                                                    "Units": "Grams"},
                                     "Onion - (in Rice)": {"Quantity": round(10 * chicken_rice_num, round_digits),
                                                                    "Units": "Grams"},
                                     }
    for ingredient, info_dict in chicken_rice_ingredients_info.items():
        st.write(ingredient, " : ", info_dict["Quantity"], " ", info_dict["Units"])


    st.write("-------------------------------------------------------------------------------------")
    # st.write("-------------------------------------------------------------------------------------")
    st.write(":blue[Ingredients  by Items]")
    # Calculations by Major Items

    chicken_qty_kgs = st.number_input("Chicken/Paneer in Kgs :chicken:", value=1.5, placeholder="Enter in Kgs")

    chicken_ingredients_info =  {"Mayo" : {"Quantity" : round((7200/120)*chicken_qty_kgs,round_digits),
                                                  "Units" : "Grams"},
                                 "Cumin" : {"Quantity" : round((960/120)*chicken_qty_kgs,round_digits),
                                                              "Units" : "Grams"},
                                 "Garlic" : {"Quantity" : round((4200/120)*chicken_qty_kgs,round_digits),
                                                                  "Units" : "Grams"},
                                 "Laung" : {"Quantity" : 3*chicken_qty_kgs,
                                                                  "Units" : "pieces"},
                                 "Black Pepper" : {"Quantity" : "Based on Taste",
                                                                  "Units" : ""}}
    for ingredient, info_dict in chicken_ingredients_info.items():
        st.write(ingredient, " : ", info_dict["Quantity"], " ", info_dict["Units"])

    st.write("-------------------------------------------------------------------------------------")

    rice_qty_kgs = st.number_input("Rice in Kgs :chicken:", value=1.5, placeholder="Enter in Kgs")

    rice_ingredients_info =  {"Cumin" : {"Quantity" : round(2*rice_qty_kgs,round_digits),
                                                  "Units" : "Grams"},
                              "Bayleaves" : {"Quantity" : round(2*rice_qty_kgs,round_digits),
                                                              "Units" : "Leaves"},
                              "Turmeric" : {"Quantity" : round(.5*rice_qty_kgs,round_digits),
                                                                  "Units" : "Grams"},
                              "Onion": {"Quantity": round((1000/6)* rice_qty_kgs, round_digits),
                                           "Units": "Grams"},
                              }
    for ingredient, info_dict in rice_ingredients_info.items():
        st.write(ingredient, " : ", info_dict["Quantity"], " ", info_dict["Units"])

    st.write("-------------------------------------------------------------------------------------")

    white_sauce_plates_num = st.number_input("White Sauce by Platters :glass_of_milk:", value=1, placeholder="Enter in Kgs")

    white_sauce_ingredients_info  =  {"Mayo" : {"Quantity" : round(33*white_sauce_plates_num,round_digits),
                                                  "Units" : "Grams"},
                              "Curd" : {"Quantity" : round(9.3*white_sauce_plates_num,round_digits),
                                                              "Units" : "Leaves"},
                              "Vinegar" : {"Quantity" : round(4*white_sauce_plates_num,round_digits),
                                                                  "Units" : "Grams"},
                              "Garlic": {"Quantity": round(.5* white_sauce_plates_num, round_digits),
                                           "Units": "Grams"},
                              "Oregano": {"Quantity": round(0.1 * white_sauce_plates_num, round_digits),
                                         "Units": "Grams"},

                              }
    for ingredient, info_dict in white_sauce_ingredients_info.items():
        st.write(ingredient, " : ", info_dict["Quantity"], " ", info_dict["Units"])



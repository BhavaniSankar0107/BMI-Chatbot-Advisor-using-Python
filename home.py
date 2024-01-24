def calculate_bmi(height, weight):
    if not (is_valid_input(height) and is_valid_input(weight)):
        raise ValueError("Invalid input. Please enter valid numeric values for height and weight.")
    return weight / (height ** 2)

def is_valid_input(value):
    return isinstance(value, (int, float)) and value > 0

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", 1
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", 2
    elif 25 <= bmi < 29.9:
        return "Overweight", 3
    elif 30 <= bmi < 34.9:
        return "Moderate Obesity", 4
    elif 35 <= bmi < 39.9:
        return "Severe Obesity", 5
    else:
        return "Very Severe or Morbid Obesity", 6

def display_steps(category):
    # Code for displaying health information based on BMI category
    if category == 1:
        print('''1. Aim to increase calorie intake through nutrient-dense foods.
        \n2. Include healthy fats, such as avocados, nuts, seeds, and olive oil.
        \n3. Consume protein-rich foods like lean meats, poultry, fish, dairy, legumes, and tofu.
        \n4. Eat frequent, balanced meals and snacks.''')
    elif category == 2:
        print('''1. Maintain a balanced diet with a mix of lean proteins, whole grains, fruits, vegetables, and healthy fats.
        \n2. Focus on portion control to prevent excessive calorie intake.
        \n3. Stay hydrated with an adequate intake of water.''')
    elif category == 3:
        print('''1. Emphasize a well-balanced diet with moderate calorie intake.
        \n2. Increase the consumption of fruits, vegetables, and whole grains.
        \n3. Choose lean protein sources and limit saturated and trans fats.
        \n4. Monitor portion sizes and be mindful of added sugars.''')
    elif category == 4:
        print('''1. Work on gradual weight loss through a balanced and calorie-controlled diet.
        \n2. Increase physical activity levels.
        \n3. Choose whole, nutrient-dense foods and limit processed and high-calorie snacks.
        \n4. Consult with a healthcare professional or dietitian for personalized guidance.''')
    elif category == 5:
        print('''1. Focus on long-term lifestyle changes, including a well-balanced diet and increased physical activity.
        \n2. Reduce intake of processed foods, sugary beverages, and high-fat snacks.
        \n3. Consider professional guidance for weight management.''')
    elif category == 6:
        print('''1. Seek professional guidance from a healthcare provider, dietitian, or weight management specialist.
        \n2. Emphasize a well-balanced, nutrient-dense diet while addressing individual health needs.
        \n3. Incorporate regular physical activity into the routine.''')

def display_diet(category):
    #code for displaying recommended diet to be followed
    if category==1:
        print('''Meal 1 (Breakfast):
            \n->Whole-grain cereal with milk and sliced bananas.
            \n->A handful of nuts or seeds.
            
            \nMeal 2 (Mid-Morning Snack):
            \n->Greek yogurt with honey and berries.
            
            \nMeal 3 (Lunch):
            \n->Grilled chicken or tofu salad with mixed greens, vegetables, and olive oil dressing.
            \n->Quinoa or brown rice on the side.
            
            \nMeal 4 (Afternoon Snack):
            \n->Whole-grain crackers with hummus.
            \n->A piece of fruit.
            
            \nMeal 5 (Dinner):
            \n->Baked salmon or lentil curry.
            \n->Sweet potato or brown rice.
            \n->Steamed vegetables.
            
            \nSnack (Evening):
            \n->Smoothie with milk, banana, and a scoop of protein powder.''')
    elif category==2:
        print('''Meal 1 (Breakfast):
            \n->Oatmeal with berries and almonds.
            \n->Low-fat Greek yogurt.
            
            \nMeal 2 (Mid-Morning Snack):
            \n->Apple slices with peanut butter.
            
            \nMeal 3 (Lunch):
            \n->Grilled chicken or chickpea salad with mixed vegetables.
            \n->Quinoa or whole-grain pasta.
            
            \nMeal 4 (Afternoon Snack):
            \n->Hummus with carrot and cucumber sticks.
            
            \nMeal 5 (Dinner):
            \n->Grilled fish or tofu.
            \n->Quinoa or sweet potato.
            \n->Steamed broccoli and asparagus.
            
            \nSnack (Evening):
            \n->Low-fat cottage cheese with pineapple.''')
    elif category==3:
        print('''Meal 1 (Breakfast):
            \n->Whole-grain toast with avocado.
            \n->Scrambled eggs or tofu.
            
            \nMeal 2 (Mid-Morning Snack):
            \n->Greek yogurt with a handful of almonds.
            
            \nMeal 3 (Lunch):
            \n->Grilled chicken or black bean salad with mixed greens.
            \n->Quinoa or brown rice.
            
            \nMeal 4 (Afternoon Snack):
            \n->Sliced cucumber with hummus.
            
            \nMeal 5 (Dinner):
            \n->Baked fish or grilled turkey.
            \n->Quinoa or wild rice.
            \n->Roasted vegetables.
            
            \nSnack (Evening):
            \n->Air-popped popcorn with a sprinkle of nutritional yeast.''')
    elif category==4:
        print('''Meal 1 (Breakfast):
            \n->Spinach and feta omelet.
            \n->Whole-grain toast.
            
            \nMeal 2 (Mid-Morning Snack):
            \n->Low-fat Greek yogurt with sliced strawberries.
            
            \nMeal 3 (Lunch):
            \n->Grilled chicken or tofu stir-fry with a variety of colorful vegetables.
            \n->Quinoa or brown rice.
            
            \nMeal 4 (Afternoon Snack):
            \n->Celery sticks with peanut butter.
            
            \nMeal 5 (Dinner):
            \n->Baked salmon or lentil stew.
            \n->Sweet potato or quinoa.
            \n->Steamed green beans and carrots.
            
            \nSnack (Evening):
            \n->Mixed nuts and seeds.''')
    elif category==5:
        print('''Meal 1 (Breakfast):
            \n->Whole-grain pancakes with fresh fruit.
            \n->Scrambled eggs or tofu.
            
            \nMeal 2 (Mid-Morning Snack):
            \n->Low-fat cottage cheese with pineapple.
            
            \nMeal 3 (Lunch):
            \n->Grilled turkey or chickpea salad with a variety of vegetables.
            \n->Quinoa or whole-grain pasta.
            
            \nMeal 4 (Afternoon Snack):
            \n->Sliced bell peppers with hummus.
            
            \nMeal 5 (Dinner):
            \n->Baked cod or grilled tempeh.
            \n->Brown rice or barley.
            \n->Steamed broccoli and cauliflower.
            
            \nSnack (Evening):
            \n->Greek yogurt with a drizzle of honey.''')
    elif category==6:
        print('''Meal 1 (Breakfast):
            \n->Veggie omelet with whole-grain toast.
            \n->Fresh fruit salad.
            
            \nMeal 2 (Mid-Morning Snack):
            \n->Mixed berries with low-fat yogurt.
            
            \nMeal 3 (Lunch):
            \n->Grilled chicken or black bean and corn salad with a variety of colorful vegetables.
            \n->Quinoa or farro.
            
            \nMeal 4 (Afternoon Snack):
            \n->Cucumber and carrot sticks with hummus.
    
            \nMeal 5 (Dinner):
            \n->Baked trout or tofu.
            \n->Sweet potato or wild rice.
            \n->Steamed Brussels sprouts and kale.
            
            \nSnack (Evening):
            \n->A small handful of almonds and walnuts.''')

def get_user_input(prompt, input_type=float):
    while True:
        try:
            user_input = input(prompt)
            if user_input.lower() == 'exit':
                exit_program()
            value = input_type(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def exit_program():
    print("\nI am glad to assist you. Thank you for using BMI Advisor.")
    exit()

# Code starts running from here
# Welcome Message
print("========  Know Your BMI Today  ========")
print("==========  Body Mass Index  ==========\n")

# Taking input Height and Weight
while True:
    try:
        h = float(input("Enter Your Height in meters: "))
        if is_valid_input(h):
            break
        else:
            print("Invalid height input.")
    except ValueError:
        print("Invalid height input.")

while True:
    try:
        w = float(input("Enter Your Weight in Kilograms: "))
        if is_valid_input(w):
            break
        else:
            print("Invalid weight input.")
    except ValueError:
        print("Invalid weight input.")
    
# Calculating BMI
BMI = calculate_bmi(h, w)
print("\nYour BMI Index value is ", BMI)

category_name, category = get_bmi_category(BMI)

print(f"\nYou are {category_name}")

while True:
    try:
        choice1 = int(input("\nIf you want to know steps to be followed for maintaining good BMI index or good health, Enter 1. To Exit, Enter 0: "))
        if choice1 == 1:
            print("\nThese are the necessary steps to be followed to maintain good health\n")
            display_steps(category)
            break
        elif choice1 == 0:
            print("\n======================================================")
            print("\nI am glad to assist you. Thank You for approaching me.\n")
            print("\n======================================================")
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if choice1 == 1:
    while True:
        try:
            choice2 = int(input("\nTo know your recommended diet Enter 1 or else to Exit Enter 0: "))
            if choice2 == 1:
                print("\nThis is the recommended diet you have to follow:\n")
                display_diet(category)
                print("\n======================================================")
                print("I am glad to assist you. Thank You for approaching me.")
                print("======================================================")
                break
            elif choice2 == 0:
                print("\n======================================================")
                print("I am glad to assist you. Thank You for approaching me.")
                print("======================================================")
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
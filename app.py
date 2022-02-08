import streamlit as st 
from PIL import Image


st.title('BMI CALCULATOR')


st.image('https://media.istockphoto.com/photos/body-mass-index-written-on-a-notepad-sheet-picture-id528072248?s=612x612')

st.markdown("Source:  [BMI Image](https://media.istockphoto.com/photos/body-mass-index-written-on-a-notepad-sheet-picture-id528072248?s=612x612)")

st.markdown('### What is BMI (Body Mass Index)? ')

st.markdown("""

	###### * Body mass index (BMI) is an assessment of body fat by calculating your height and weight. 

	###### * It doesn’t measure body fat directly, but it uses an equation to make an approximation. 

	###### * BMI can help to find out if a person is at an unhealthy or healthy weight. 

	"""
	)


with st.expander('Click here to know more about BMI'):

	st.markdown(""" 

	###### * BMI shows the link between your height and weight as a single number that is not dependent on “frame size.” 

	###### * Even though the creation of the BMI is over 200 years old, it is relatively new as a measure of health.

	###### * There are certain A high BMI can be a symptom of too much fat on your body. Meanwhile, a low BMI can be a symptom of too little fat on the body. 

	###### * The higher your BMI result, the higher your possibilities of getting certain severe conditions, such as heart disease, high blood pressure, and diabetes. 

	###### * A very low BMI can also become the cause of health problems, including bone loss, decreased immune function, and anemia.

	###### * While BMI can be helpful, it actually has limitations.

	###### * BMI may exaggerate the amount of body fat in athletes and other people with very muscular bodies. 

	###### * It may also undervalue the amount of body fat in older adults and other people who have lost muscle mass.

	###### * However, it’s useful as a first attempt to evaluate your overall health (you might not want to see a doctor yet if you’re not sure if you’re healthy or not).

	`Information Credits`: https://www.quora.com/What-is-Body-Mass-Index-BMI-Is-it-scientific-Is-it-an-estimation-only/answer/Kirei-Living
	"""
	
	)


st.markdown('#### Disclaimer:')

st.markdown("""

	###### * The Author is not a Doctor
	
	###### * This tool is just a showcase of practical experience in Python and Streamlit

	###### * You should always consult a Doctor to get your Health Check

	###### * Please don't take the outcome of this tool seriously and NEVER consider it Valid

	"""
	)



# Input
#..........................................................................................................

st.markdown('### Check your BMI here:')

weight = st.number_input("Enter your Weight in Kilograms", 0.0, 1000.0, step = 0.1)

height = st.number_input("Enter your Height in Meters", 0.0, 1000.5)

BMI = weight/(height*height)


if BMI <= 18.4:

	st.warning('You are Underweight with an BMI score of {}' .format(round(BMI, 2)))

	st.markdown('### Tips to gain Weight:')

	st.markdown("""

			###### * Eat more frequently

			###### * Choose Nutrition Rich Foods

			###### * Try Smoothies and Shakes

			###### * Exercise regularly

			"""
			)

	st.markdown('#### Healthy High Calorie Foods for Weight Gain:')
	st.image('https://miro.medium.com/max/600/1*cwDSsUF8XcxFpc7Yz_9B1A.jpeg')
	st.markdown("Source: [Healthy High Calorie Foods for Weight Gain](https://miro.medium.com/max/600/1*cwDSsUF8XcxFpc7Yz_9B1A.jpeg)")
    

elif BMI <= 24.9:

	st.success('You are Healthy with an BMI score of {}' .format(round(BMI, 2)))

	st.markdown('### Awesome! You are at an Healthy Weight. However, you can follow these tips to keep your Health Intact:')

	st.markdown("""

			###### * Eat good foods

			###### * Stay Hydrated

			###### * Sleep well

			###### * Exercise regularly

			"""
			)

	st.markdown('#### The greatest Wealth is Health :')
	st.image('https://blogs.biomedcentral.com/on-medicine/wp-content/uploads/sites/6/2019/09/iStock-1131794876.t5d482e40.m800.xtDADj9SvTVFjzuNeGuNUUGY4tm5d6UGU5tkKM0s3iPk-620x342.jpg')
	st.markdown("Source: [Healthy Food](https://blogs.biomedcentral.com/on-medicine/wp-content/uploads/sites/6/2019/09/iStock-1131794876.t5d482e40.m800.xtDADj9SvTVFjzuNeGuNUUGY4tm5d6UGU5tkKM0s3iPk-620x342.jpg)")
    

elif BMI <= 29.9:

	st.warning('You are Overweight with an BMI score of {}' .format(round(BMI, 2)))

	st.markdown('### Tips to help you lose weight:')

	st.markdown("""

			###### * Do not skip Breakfast. You could miss out on essential nutrients and you may end up snacking more throughout the day because you feel hungry

			###### * Stay Hydrated

			###### * Eat plenty of Fruits and Vegetables

			###### * Say no to Junk Food

			###### * Eat high Fibre Foods

			###### * Exercise regularly

			"""
			)

	st.markdown('#### Foods that help you to lose Weight :')
	st.image('https://99healthyfood.files.wordpress.com/2018/11/the-foods-help-to-loss-weight.jpg?w=720')
	st.markdown("Source: [Weight Loss Foods](https://99healthyfood.files.wordpress.com/2018/11/the-foods-help-to-loss-weight.jpg?w=720)")
    

else:

	st.error('You are Obese with an BMI score of {}' .format(round(BMI, 2)))

	st.markdown('### Tips to help you lose Obesity:')

	st.markdown("""

			###### * Consume less processed and sugary foods

			###### * Stay Hydrated

			###### * Eat plenty of Fruits and Vegetables

			###### * Say no to Junk Food

			###### * Eat plenty of dietary Fibre

			###### * Exercise regularly

			###### * Consult a Nutritionist or Doctor and follow 'Weight loss program'

			"""
			)

	st.markdown('#### Foods to help you lose Obesity :')
	st.image('https://i.pinimg.com/736x/90/65/d3/9065d3f60cd41a2ce92630be2b81ed5f.jpg')
	st.markdown("Source: [Foods for preventing Obesity](https://i.pinimg.com/736x/90/65/d3/9065d3f60cd41a2ce92630be2b81ed5f.jpg)")

    
img = Image.open('IMG_6959.jpg')

st.sidebar.header('About the Author:')
st.sidebar.image(img)
st.sidebar.markdown('## Karthik Thallam')
st.sidebar.markdown('##### Machine Learning Engineer')

st.sidebar.caption('Wish to connect?')

st.sidebar.markdown('Linkedin : [Karthik Thallam](https://www.linkedin.com/in/karthikthallam/)')
st.sidebar.write('📧: karthik.thallam1@gmail.com')



























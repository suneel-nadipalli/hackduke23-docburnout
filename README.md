# Inspiration
Upon listening to Dr. Luis' talk, our team realized the urgency of reducing patient deaths due to a medical error. In the United States medical errors are the third leading cause of patient deaths, resulting in 250,00 incidents every year. Recognizing the potential impact, we dove into designing and implementing a solution for this problem.

# What it does
Most medical errors come from human errors, which can be prevented by addressing healthcare worker stress and burnout. To combat this, we designed and built an application that:

- Employs machine learning to monitor health signals, including heart rate, body oxygen, body temperature, and respiration rate, in order to calculate a stress score
- Tests for burnout identification using the highly researched MBI Medical Practitioner test
- Evaluates fatigue using facial image capture (Proof of Concept)
- Suggests tips to reduce stress and burnout
- We aim to increase healthcare worker awareness regarding their stress and burnout levels, in order to increase the quality of decisions and improve patient outcomes.

# How we built it
We implemented the application using a Streamlit app for a proof of concept. We trained the ML model in a Google Collab, saving a pickl file for access during inference.

# Challenges we ran into
One of the main challenges we ran into was sourcing the data to train the model. It was challenging to find accessible healthcare setting data to predict stress and burnout levels. We trained our model using data from a sleep stress detection study as a proof of concept. In the future, we plan to obtain and train on real-time data from a healthcare setting.

Another challenge we ran into was that our team was made up of data scientists, not full-stack developers. As such, we decided to implement a lightweight prototype app using Streamlit.

# Accomplishments that we're proud of
We're most proud of building a solution that solves a well-framed, meaningful problem. We believe our solution has potential to reduce the number of patient deaths due to medical error because we address a major root cause: healthcare worker burnout.

We are also proud of our team’s grit, determination, and resourcefulness to build a prototype of our solution in such a short timeframe.

# What we learned
We learned the importance of solving well-framed, specific problems and how that can translate to efficient product development. We focused on building an application with few but effective features.

Our team also deepened our knowledge of Streamlit, enabling quick prototyping and deployment.

# What's next for patteRN Health
Next steps for patteRN Health include building a comprehensive prototype using React Native and a more complex machine learning model by continuously sourcing relevant data from the app. This would improve our solution, provide more valuable insights to users and provide us an opportunity to acquire more mobile app development skills.

# Built With
- Python
- Pandas
- NumPy
- Streamlit
- Scikit-Learn

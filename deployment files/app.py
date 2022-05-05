import pandas as pd
import streamlit as st
import pickle
from iteration_utilities import unique_everseen
from iteration_utilities import duplicates

nav = st.sidebar.selectbox('PLEASE SELECT WHAT YOU ARE LOOKING FOR',["HOME", "JOB"])

if nav == "HOME":
    st.markdown("""<h1 align="Center"><font face="Garamond" color="#4863A0"><b>CARRIER  RECOMMENDATION SYSTEM</b></font></h1>""",True)

# @@@@@@@@ SETTING JOB PAGE
if nav == "JOB":
    st.markdown("""<h2 align="Left"><font face="Times New Roman" color="#4863A0">Job Recommendation System<b></b></font></h2>""",True)


    def recommend(job_name):
        job_index = job1[job1['KEY_SKILL'] == job_name].index[0]
        distances = similarity[job_index]
        job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_job = []
        for i in job_list:
            recommended_job.append(job1.iloc[i[0]].JOB_TYPE)
        recommended_job1 = set(recommended_job)
        return recommended_job1


    def recommend_ug(job_name):
        job_index = job1[job1['UG'] == job_name].index[0]
        distances = similarity[job_index]
        job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_job = []
        for i in job_list:
            recommended_job.append(job1.iloc[i[0]].JOB_TYPE)
        recommended_job1 = set(recommended_job)
        return recommended_job1


    def recommend_spe(job_name):
        job_index = job1[job1['SPECIALIZATION'] == job_name].index[0]
        distances = similarity[job_index]
        job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_job = []
        for i in job_list:
            recommended_job.append(job1.iloc[i[0]].JOB_TYPE)
        recommended_job1 = set(recommended_job)
        return recommended_job1


    def recommend_inti(job_name):
        job_index = job1[job1['INTERESTS'] == job_name].index[0]
        distances = similarity[job_index]
        job_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:15]

        recommended_job = []
        for i in job_list:
            recommended_job.append(job1.iloc[i[0]].JOB_TYPE)
        recommended_job1 = set(recommended_job)
        return recommended_job1


    job_list = pickle.load(open(r'job_rec.pkl', 'rb'))
    job1 = pd.DataFrame(job_list)
    similarity = pickle.load(open(r'similarity_func.pkl', 'rb'))

    UG1 = set(job1['UG'].values)
    selected_ug = st.selectbox('Please select your Under Graduate Programme',UG1)

    SPEC1 = set(job1['SPECIALIZATION'].values)
    selected_Specialization = st.selectbox('Please select your specialization',SPEC1)

    SPEC2 = set(job1['KEY_SKILL'].values)

    key_skill = st.multiselect('Select Your Skills', SPEC2)
    skill = pd.Series(key_skill)
    skill_1 = skill.values
    container = st.container()

    SPEC3 = set(job1['INTERESTS'].values)
    INTERESTS = st.multiselect('Select Your Interests', SPEC3)
    interest = pd.Series(INTERESTS)
    skill_2 = interest.values

    if st.button('Recommend'):
        recommendation = []

        for i in skill_1:
            recommendation.extend(recommend(i))

        for i in skill_2:
            recommendation.extend(recommend_inti(i))
        recommendation.extend(recommend_ug(selected_ug))
        recommendation.extend(recommend_spe(selected_Specialization))
        result = pd.DataFrame(unique_everseen(duplicates(recommendation)))
        result = result.rename(columns={0: "Recommended Jobs for you"})

        st.write(result[1:16])


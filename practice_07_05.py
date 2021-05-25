# 입출력_with

# import pickle

# with open("profile.pickle", "rb")as profile_file:
#     print(pickle.load(profile_file))

with open("study.txt", "r", encoding="uft8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="uft8") as study_file:
    print(study_file.read())    
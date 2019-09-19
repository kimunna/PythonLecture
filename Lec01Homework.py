name = input("이름 : ")
scienceScore = int(input("과학성적 : "))
mathScore = int(input("수학성적 : "))
englishScore = int(input("영어성적 : "))
totalScore = scienceScore + mathScore + englishScore
averageScore = float(totalScore/3.0)
print("이름 : ", name)
print("총점 : ", totalScore)
print("평균 : ", averageScore)
i = 1
studentList = []

telebeSayi = int(input("Qupdakı tələbələrin sayını daxil edin: "))

while i<= telebeSayi:
    print(f"{i}-ci tələbənin məlumatlarını daxil edin: ")
    i+=1
    _id = int(input("Tələbənin İD-si: "))
    _ad = input("Tələbənin Adı: ")
    _soyad = input("Tələbənin Soyadı: ")
    _email  = input("Tələbənin e-maili: ")
    _contact = int(input("Tələbəlin telefon nömrəsi: "))
    student = {
        'id': _id,
        'name': _ad,
        'surname': _soyad,
        'email': _email,
        'contact': _contact
    }

    studentList.append(student)
    Davam = int(input("Novbəti tələbənin məlumatlarını daxil etmek isteyirsinizse 1 yazin\nSonlamaq isteyirsizse 2 yazin :"))
    if Davam == 1:
        continue
    else:
        break

for _student in studentList:
    print(f" Tələbənin İD-si: {_student['id']}\n Tələbənin Adı: {_student['name']}\n Tələbənin Soyadı: {_student['surname']}\n Tələbənin e-maili: {_student['email']}\n Tələbəlin telefon nömrəsi: {_student['contact']}")
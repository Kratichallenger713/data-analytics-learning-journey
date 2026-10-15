f =open("FileInputOutput/student.txt","a")
student=[
    "\nKratika Bathav\n",
    "Arpit Mittal\n"
]
f.writelines(student)
f.close()
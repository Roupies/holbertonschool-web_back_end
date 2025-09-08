function updateStudentGradeByCity(students, city, grades) {
    if (!Array.isArray(students)) return [];
    return students
        .filter((student) => student.location === city)
        .map((student) => {
            const updatedStudent = { ...student };
            const gradeObj = Array.isArray(grades)
                ? grades.find((g) => g.studentId === student.id)
                : undefined;
            updatedStudent.grade = gradeObj ? gradeObj.grade : 'N/A';
            return updatedStudent;
        });
}

export default updateStudentGradeByCity;
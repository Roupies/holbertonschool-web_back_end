function updateStudentGradeByCity(students, city, newGrade) {
    if (!Array.isArray(students)) return [];
    return students
        .filter((student) => student.location === city)
        .map((student) => {
            const updatedStudent = { ...student };
            if (newGrade !== undefined) {
                updatedStudent.grade = newGrade;
            } else {
                updatedStudent.grade = 'N/A';
            }
            return updatedStudent;
        });
}

export default updateStudentGradeByCity;
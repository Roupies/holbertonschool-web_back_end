import getListStudents from './0-get_list_students';

function getListStudentIds() {
    const students = getListStudents();
    return students.map((student) => student.id);
}

export default getListStudentIds;
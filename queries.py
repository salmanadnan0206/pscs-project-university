import datetime
import sys
import traceback

from student_database import session, Student, CourseList, Course, Activity


# main_glob_id = 20180

class AllQueries:
    def __init__(self):
        self.glob_id = 20180

    # def email_and_password(self, std_id):
    def email_and_password(self):
        std_id = self.glob_id
        student = session.query(Student).filter_by(std_id=std_id).first()
        return student.email, student.password

    def get_std_id(self):
        return self.glob_id

    def get_std_id_by_email(self, email):
        student = session.query(Student).filter_by(email=email).first()
        return student.std_id

    def get_password_by_email(self, email):
        student = session.query(Student).filter_by(email=email).first()
        if student is None:
            return None
        return student.password

    def get_course_by_id(self, course_id):
        # Get the course from course_list
        course = session.query(CourseList).filter_by(course_list_id=course_id).first()
        return course

    def update_std_id(self, std_id):
        # main_glob_id = std_id
        self.glob_id = std_id

    def get_current_day(self):
        # Get the current day
        current_day = datetime.datetime.now().strftime("%A")
        return current_day

    def get_all_courses(self):
        # Get all the courses from course_list
        course_list = session.query(CourseList).all()
        return course_list

    def get_course_by_std_id_and_course_id(self, course_id):
        std_id = self.glob_id
        # Get the course from course_list
        print()
        print()
        print(f"std_id: {std_id}\ncourse_id: {course_id}")
        course = session.query(Course).filter_by(std_id=std_id, course_id=course_id,
                                                 is_temp=False).first()
        return course

    def get_course_by_id_and_section(self, course_id, section):
        # Get the course from course_list
        course = session.query(CourseList).filter_by(course_list_id=course_id,
                                                     section=section).first()
        return course

    # def get_all_courses_by_id(self, std_id):
    def get_all_courses_by_id(self):
        std_id = self.glob_id
        print()
        print()
        print("std_id: " + str(std_id))
        print("self.glob_id: " + str(self.glob_id))
        # Get all the courses from course_list
        course_list = session.query(Course).filter_by(std_id=std_id, is_temp=False).all()
        return course_list

    # def get_all_courses_by_std_id_and_course_id(self, std_id, course_id):
    def get_all_courses_by_std_id_and_course_id(self, course_id):
        std_id = self.glob_id
        # Get all the courses from course_list
        course_list = session.query(Course).filter_by(std_id=std_id, course_id=course_id, is_temp=False).all()
        return course_list

    # def get_all_courses_by_id_and_type(self, std_id, type):
    def get_all_courses_by_id_and_type(self, type):
        std_id = self.glob_id
        print(self.glob_id)
        # Get all the courses from course_list
        course_list = session.query(Course).filter_by(std_id=std_id, type=type).all()
        print("course_list: " + str(course_list))
        print("std_id: " + str(std_id))
        print("type: " + str(type))
        return course_list

    # def check_if_course_already_exist(self, course_id, section):
    def check_if_course_already_exist(self, course_id, section):
        std_id = self.glob_id
        # Get the course from course_list
        course = session.query(Course).filter_by(std_id=std_id, course_id=course_id,
                                                 section=section).first()
        if course is None:
            return False
        else:
            return True

    def is_user_enrolled_in_this_course(self, course_id, section):
        std_id = self.glob_id
        # Get the course from course_list
        course = session.query(Course).filter_by(std_id=std_id, course_id=course_id,
                                                 section=section, is_temp=False).first()
        if course is None:
            return False
        else:
            return True

    def time_to_seconds(self, t):
        return t.hour * 3600 + t.minute * 60 + t.second

    def get_timings_of_all_courses_by_id(self, exclude_id, exclude_section):
        # Get the timings of all the courses from courses for a particular student in seconds
        std_id = self.glob_id
        course_list = session.query(Course).filter_by(std_id=std_id, is_temp=False).all()
        start_timings = []
        end_timings = []
        days = []
        for course in course_list:
            course_list = session.query(CourseList).filter_by(course_list_id=course.course_id,
                                                              section=course.section).first()
            # timings.append(course_list.end_time - course_list.start_time)

            if course.course_id == exclude_id and course.section == exclude_section:
                continue

            end_time = course_list.end_time
            start_time = course_list.start_time
            day = course_list.days

            print(end_time)
            print(start_time)
            print(day)

            end_time = self.time_to_seconds(end_time)
            start_time = self.time_to_seconds(start_time)

            end_timings.append(end_time)
            start_timings.append(start_time)
            days.append(day)

            print(end_time)
            print(start_time)
            print(day)
            print(type(end_time))
            print(type(start_time))
            print(type(day))
        print()
        print()
        print()
        print()

        # # Convert the time in seconds
        # for i in range(len(timings)):
        #     timings[i] = timings[i].seconds

        return start_timings, end_timings, days

    def get_days_timings_of_all_courses_by_id_temp_false(self):
        # Get the timings of all the courses from courses for a particular student in seconds
        std_id = self.glob_id
        course_list = session.query(Course).filter_by(std_id=std_id).all()
        days = []
        start_timings = []
        end_timings = []
        for course in course_list:
            course_list = session.query(CourseList).filter_by(course_list_id=course.course_id,
                                                              section=course.section).first()
            # timings.append(course_list.end_time - course_list.start_time)
            end_time = course_list.end_time
            start_time = course_list.start_time
            day = course_list.days

            print(end_time)
            print(start_time)
            print(day)

            end_time = self.time_to_seconds(end_time)
            start_time = self.time_to_seconds(start_time)

            end_timings.append(end_time)
            start_timings.append(start_time)
            days.append(day)

            print(end_time)
            print(start_time)
            print(day)
            print(type(end_time))
            print(type(start_time))
            print(type(day))
        print()
        print()

        # # Convert the time in seconds
        # for i in range(len(timings)):
        #     timings[i] = timings[i].seconds

        return start_timings, end_timings, days

    def get_days_list(self, days):
        return [days[x:x + 2] for x in range(0, len(days), 2)]

    # def add_course(self, std_id, course_list_id, section):
    def add_course(self, course_list_id, section):
        std_id = self.glob_id
        # Get the course from course_list
        course = session.query(CourseList).filter_by(course_list_id=course_list_id).first()
        print("course.section: " + course.section)

        # is_already_added = self.check_if_course_already_exist(std_id, course_list_id, section)
        is_already_added = self.check_if_course_already_exist(course_list_id, section)
        if is_already_added:
            print("Returning false")
            return False

        # Create a new course object
        new_course = Course(std_id=std_id, section=section, course_id=course_list_id,
                            is_temp=True, type="Add")
        # Add the course to the database
        session.add(new_course)
        # Commit the changes
        try:
            session.commit()
        except:
            print("Error: " + str(sys.exc_info()[0]))
            print(traceback.format_exc())
            # undo the changes
            session.rollback()
            return False
        return True

    # def remove_course(self, std_id, course_id, section):
    def remove_course(self, course_id, section):
        std_id = self.glob_id
        # Get the course from course_list
        print("Came in here")
        course = session.query(Course).filter_by(std_id=std_id, course_id=course_id, section=section).first()
        # Delete the course from the database
        print()
        print()
        print(" std_id: " + str(std_id)
              + " course_id: " + str(course_id)
              + " section: " + str(section))
        session.delete(course)
        # Commit the changes
        try:
            session.commit()
        except:
            print("Error: " + str(sys.exc_info()[0]))
            print(traceback.format_exc())
            # undo the changes
            session.rollback()
            return False
        return True

    # def is_temp_false_remove_type_add(self, std_id, course_type):
    def is_temp_false_remove_type_add(self, course_type):
        std_id = self.glob_id
        # Get the course from course_list
        course = session.query(Course).filter_by(std_id=std_id, type=course_type).all()
        # course.is_temp = False
        # course.type = None
        for c in course:
            c.is_temp = False
            c.type = None

        # Commit the changes
        try:
            session.commit()
        except:
            print("Error: " + str(sys.exc_info()[0]))
            print(traceback.format_exc())
            # undo the changes
            session.rollback()
            return False
        return True

    # def is_temp_false_single_course(self, std_id, course_id, section):
    def is_temp_false_single_course(self, course_id, section):
        std_id = self.glob_id
        # Get the course from course_list
        course = session.query(Course).filter_by(std_id=std_id, course_id=course_id,
                                                 section=section).first()
        # course.is_temp = False
        # course.type = None
        course.is_temp = False
        course.type = None

        # Commit the changes
        try:
            session.commit()
        except:
            print("Error: " + str(sys.exc_info()[0]))
            print(traceback.format_exc())
            # undo the changes
            session.rollback()
            return False
        return True

    def update_current_capacity(self, course_id, section, add_or_subtract):
        # Get the course from course_list
        course = session.query(CourseList).filter_by(course_list_id=course_id,
                                                     section=section).first()
        if add_or_subtract == "Add":
            course.current_capacity += 1
        elif add_or_subtract == "Subtract":
            course.current_capacity -= 1

        if course.current_capacity == 0:
            course.status = False
        elif course.current_capacity > 0:
            course.status = True
        else:
            print("Error: current_capacity is negative")
            return False

        # Commit the changes
        try:
            session.commit()
        except:
            print("Error: " + str(sys.exc_info()[0]))
            print(traceback.format_exc())
            # undo the changes
            session.rollback()
            return False
        return True

    # def swap_courses(self, std_id, course_id, section, course_id_enrolled, section_enrolled):
    def swap_courses(self, course_id, section, course_id_enrolled, section_enrolled):
        std_id = self.glob_id
        # Remove the enrolled course
        print(f"std_id: {std_id}\ncourse_id: {course_id}\nsection: {section}")
        # self.remove_course(std_id, course_id_enrolled, section_enrolled)
        self.remove_course(course_id_enrolled, section_enrolled)

        # Add the course
        try:
            # does_it_work = self.add_course(20180, int(course_id), section)
            # does_it_work = self.add_course(std_id, int(course_id), section)
            does_it_work = self.add_course(int(course_id), section)
            if not does_it_work:
                print()
                print()
                print("Course could not be added")
                return False
            # self.is_temp_false_single_course(std_id, course_id, section)
            self.is_temp_false_single_course(course_id, section)
        except:
            print("Error: " + str(sys.exc_info()[0]))
            print(traceback.format_exc())
            print("Return is being called")
            return
        return True

    def get_activity_by_std_id(self):
        std_id = self.glob_id
        # Get the course from course_list
        activity = session.query(Activity).filter_by(std_id=std_id).all()
        return activity

    def add_data_to_activity_log(self, std_id, activity_type, course_id=None, section=None):
        # Get the course from course_list
        course = session.query(CourseList).filter_by(course_list_id=course_id).first()
        # Create a new course object
        new_activity = Activity(std_id=std_id, course_id=str(course_id), activity_type=activity_type,
                                activity_date=datetime.datetime.now().date(),
                                activity_time=datetime.datetime.now().time(),
                                course_section=section)
        # Add the course to the database
        session.add(new_activity)
        # Commit the changes
        try:
            session.commit()
        except:
            print("Error: " + str(sys.exc_info()[0]))
            print(traceback.format_exc())
            # undo the changes
            session.rollback()
            return False
        return True

    def delete_all_data_activity_log(self):
        # Get the course from course_list
        activity = session.query(Activity).all()
        # Create a new course object
        for a in activity:
            session.delete(a)
        # Add the course to the database
        # Commit the changes
        try:
            session.commit()
        except:
            print("Error: " + str(sys.exc_info()[0]))
            print(traceback.format_exc())
            # undo the changes
            session.rollback()
            return False
        return True

    def delete_everything_in_course_table(self):
        # Get the course from course_list
        course = session.query(Course).all()
        # Create a new course object
        for c in course:
            session.delete(c)
        # Add the course to the database
        # Commit the changes
        try:
            session.commit()
        except:
            print("Error: " + str(sys.exc_info()[0]))
            print(traceback.format_exc())
            # undo the changes
            session.rollback()
            return False
        return True


if __name__ == "__main__":
    all_queries = AllQueries()
    all_queries.delete_all_data_activity_log()
    all_queries.delete_everything_in_course_table()
    print(all_queries.get_current_day())

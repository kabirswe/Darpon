from __future__ import unicode_literals

from django.db import models


class Aboutus(models.Model):
    picture = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'aboutus'


class Academiccalender(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    descriptionfile = models.CharField(max_length=30)
    academiccalendertypeid = models.ForeignKey('Academiccalendertype', models.DO_NOTHING, db_column='academiccalendertypeid')
    cdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'academiccalender'


class Academiccalendertype(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'academiccalendertype'


class Administration(models.Model):
    name = models.CharField(max_length=200)
    picture = models.CharField(max_length=30)
    description = models.CharField(max_length=20)
    person = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'administration'


class Adminlogin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    usertype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'adminlogin'


class Assigningclassforstudent(models.Model):
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentid')
    classid = models.ForeignKey('Class', models.DO_NOTHING, db_column='classid')
    classroll = models.IntegerField()
    yearid = models.ForeignKey('Year', models.DO_NOTHING, db_column='yearid')
    sectionid = models.ForeignKey('Section', models.DO_NOTHING, db_column='sectionid')
    shiftid = models.ForeignKey('Shift', models.DO_NOTHING, db_column='shiftid')
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherid')
    date = models.DateTimeField()
    group = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'assigningclassforstudent'
        unique_together = (('studentid', 'classid', 'yearid', 'shiftid', 'sectionid'),)


class Assigningclassteacher(models.Model):
    teacherid = models.IntegerField()
    classid = models.IntegerField()
    sectionid = models.IntegerField()
    shiftid = models.IntegerField()
    yearid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assigningclassteacher'


class Assigningteacher(models.Model):
    classid = models.IntegerField()
    teacherid = models.CharField(max_length=10)
    yearid = models.CharField(max_length=5)
    subjectid = models.IntegerField()
    shiftid = models.IntegerField()
    sectionid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assigningteacher'


class Attendence(models.Model):
    studentid = models.IntegerField()
    classid = models.IntegerField()
    yearid = models.IntegerField()
    teacherid = models.IntegerField()
    sectionid = models.IntegerField()
    shiftid = models.IntegerField()
    examnameid = models.IntegerField()
    present = models.CharField(max_length=5)
    absent = models.CharField(max_length=5)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'attendence'


class Blog(models.Model):
    studentid = models.IntegerField(blank=True, null=True)
    teacherid = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=20)
    cdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blog'


class Bloodgroup(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'bloodgroup'


class Boardresult(models.Model):
    studentname = models.CharField(max_length=30)
    registrationno = models.CharField(max_length=20)
    rollno = models.CharField(max_length=20)
    cgpa = models.CharField(max_length=10)
    examtype = models.CharField(max_length=10)
    year = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'boardresult'


class Class(models.Model):
    name = models.CharField(max_length=25)
    groups = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'class'


class Classblog(models.Model):
    studentid = models.IntegerField(blank=True, null=True)
    teacherid = models.IntegerField(blank=True, null=True)
    classid = models.IntegerField()
    description = models.CharField(max_length=40)
    cdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'classblog'


class Classmaterial(models.Model):
    classid = models.IntegerField()
    classmaterialtypeid = models.IntegerField()
    docfile = models.CharField(max_length=30)
    assigningteacherid = models.IntegerField()
    description = models.CharField(max_length=50)
    cdate = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'classmaterial'


class Classmaterialtype(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'classmaterialtype'


class Contactus(models.Model):
    description = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'contactus'


class Contactususer(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=20)
    contactnumber = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    messagesubject = models.CharField(max_length=40)
    message = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'contactususer'


class District(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'district'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Earn(models.Model):
    amount = models.CharField(max_length=20)
    earntypeid = models.IntegerField()
    dayid = models.IntegerField()
    monthid = models.IntegerField()
    yearid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'earn'


class Earntype(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'earntype'


class Examname(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'examname'


class Expence(models.Model):
    amount = models.CharField(max_length=20)
    expencetypeid = models.IntegerField()
    dayid = models.IntegerField()
    monthid = models.IntegerField()
    yearid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'expence'


class Expenceforgardiantarrangement(models.Model):
    amount = models.CharField(max_length=10)
    expenceforgardiantarrangementtypeid = models.IntegerField()
    dayid = models.IntegerField()
    monthid = models.IntegerField()
    yearid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'expenceforgardiantarrangement'


class Expenceforgardiantarrangementtype(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'expenceforgardiantarrangementtype'


class Expenceforpublish(models.Model):
    amount = models.CharField(max_length=10)
    expenceforpublishtypeid = models.IntegerField()
    dayid = models.IntegerField()
    monthid = models.IntegerField()
    yearid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'expenceforpublish'


class Expenceforpublishtype(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'expenceforpublishtype'


class Expencetype(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'expencetype'


class Gardianmember(models.Model):
    name = models.CharField(max_length=30)
    picture = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    description = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'gardianmember'


class Hitcounter(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    countnumber = models.IntegerField(db_column='CountNumber')  # Field name made lowercase.
    hitdate = models.DateField(db_column='HitDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hitcounter'


class Homewelcome(models.Model):
    name = models.CharField(max_length=3000)
    type = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'homewelcome'


class Iqtest(models.Model):
    questionno = models.CharField(max_length=25)
    subjectnameid = models.IntegerField()
    question = models.CharField(max_length=25)
    option1 = models.CharField(max_length=25)
    option2 = models.CharField(max_length=25)
    option3 = models.CharField(max_length=25)
    option4 = models.CharField(max_length=25)
    answer = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'iqtest'


class News(models.Model):
    headline = models.CharField(max_length=50)
    description = models.CharField(max_length=30)
    picture = models.CharField(max_length=40)
    cdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'news'


class Noticbord(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=30)
    descriptionfile = models.CharField(max_length=50)
    notictypeid = models.IntegerField()
    cdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'noticbord'


class Notictype(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'notictype'


class Onlineregistration(models.Model):
    studentid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    picture = models.CharField(max_length=40)
    classid = models.CharField(max_length=14)
    fname = models.CharField(max_length=25)
    mname = models.CharField(max_length=25)
    gender = models.CharField(max_length=5)
    nationality = models.CharField(max_length=10)
    religionid = models.IntegerField()
    bloodgroupid = models.IntegerField()
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    previousinstitute = models.CharField(max_length=40)
    paddress = models.CharField(max_length=1000)
    peraddress = models.CharField(max_length=1000)
    tcno = models.CharField(max_length=20)
    previousresult = models.CharField(max_length=20)
    transport = models.CharField(max_length=30)
    wishclass = models.CharField(max_length=100)
    fromtransport = models.CharField(max_length=100)
    districtid = models.IntegerField()
    thanaid = models.IntegerField()
    villageid = models.IntegerField()
    dateofbirth = models.DateField()
    joindate = models.DateField()

    class Meta:
        managed = False
        db_table = 'onlineregistration'


class Paidamount(models.Model):
    studentid = models.CharField(max_length=10)
    classid = models.IntegerField()
    dayid = models.IntegerField()
    monthid = models.CharField(max_length=15)
    yearid = models.IntegerField()
    shiftid = models.IntegerField()
    sectionid = models.IntegerField()
    payorpaidamounttypeid = models.IntegerField()
    examnameid = models.IntegerField()
    amount = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'paidamount'


class Payableamount(models.Model):
    classid = models.IntegerField()
    dayid = models.IntegerField()
    monthid = models.IntegerField()
    yearid = models.IntegerField()
    shiftid = models.IntegerField()
    payorpaidamounttypeid = models.IntegerField()
    amount = models.CharField(max_length=10)
    examnameid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payableamount'
        unique_together = (('classid', 'yearid', 'shiftid', 'examnameid', 'payorpaidamounttypeid'),)


class Payorpaidamounttype(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'payorpaidamounttype'


class Photogallary(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    picture = models.CharField(max_length=30, blank=True, null=True)
    phototypeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'photogallary'


class Photoslider(models.Model):
    headline = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    picture = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'photoslider'


class Phototype(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'phototype'


class Religion(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'religion'


class Result(models.Model):
    studentid = models.CharField(max_length=10)
    classid = models.IntegerField()
    subjectid = models.IntegerField()
    yearid = models.IntegerField()
    teacherid = models.CharField(max_length=10)
    sectionid = models.IntegerField()
    shiftid = models.IntegerField()
    fullmarks = models.CharField(max_length=10)
    number_1stclasstest = models.CharField(db_column='1stClassTest', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndclasstest = models.CharField(db_column='2ndClassTest', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1sttermexam = models.CharField(db_column='1stTermExam', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1sttermfullmarks = models.CharField(db_column='1stTermFullMarks', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdclasstest = models.CharField(db_column='3rdClassTest', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4thclasstest = models.CharField(db_column='4thClassTest', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndtermexam = models.CharField(db_column='2ndTermExam', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndtermfullmarks = models.CharField(db_column='2ndTermFullMarks', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5thclasstest = models.CharField(db_column='5thClassTest', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6thclasstest = models.CharField(db_column='6thClassTest', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdtermexam = models.CharField(db_column='3rdTermExam', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdtermfullmarks = models.CharField(db_column='3rdTermFullMarks', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_7thclasstest = models.CharField(db_column='7thClassTest', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_8thclasstest = models.CharField(db_column='8thClassTest', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4thtermexam = models.CharField(db_column='4thTermExam', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4thtermfullmarks = models.CharField(db_column='4thTermFullMarks', max_length=5)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    totalmarks = models.CharField(db_column='totalMarks', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'result'
        unique_together = (('studentid', 'classid', 'yearid', 'subjectid'),)


class Schoolcontact(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    teln = models.CharField(max_length=15)
    mobn = models.CharField(max_length=15)
    fax = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'schoolcontact'


class Section(models.Model):
    name = models.CharField(max_length=25)
    shiftid = models.IntegerField()
    classid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'section'


class Shift(models.Model):
    name = models.CharField(max_length=25)
    classid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shift'


class Student(models.Model):
    studentid = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=25)
    picture = models.CharField(max_length=40)
    classid = models.CharField(max_length=14)
    fname = models.CharField(max_length=25)
    mname = models.CharField(max_length=25)
    gender = models.CharField(max_length=5)
    nationality = models.CharField(max_length=10)
    religionid = models.IntegerField()
    bloodgroupid = models.IntegerField()
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    previousinstitute = models.CharField(max_length=40)
    paddress = models.CharField(max_length=1000)
    peraddress = models.CharField(max_length=1000)
    tcno = models.CharField(max_length=20)
    previousresult = models.CharField(max_length=20)
    transport = models.CharField(max_length=30)
    wishclass = models.CharField(max_length=100)
    fromtransport = models.CharField(max_length=100)
    districtid = models.IntegerField()
    thanaid = models.IntegerField()
    villageid = models.IntegerField()
    dateofbirth = models.DateField()
    joindate = models.DateField()

    class Meta:
        managed = False
        db_table = 'student'


class Subject(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    classid = models.IntegerField(blank=True, null=True)
    groups = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'subject'


class SubjectQuestion(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'subject_question'


class Superadminlogin(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'superadminlogin'


class Talentstudent(models.Model):
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    address = models.CharField(max_length=40)
    description = models.CharField(max_length=30)
    picture = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'talentstudent'


class Talentteacher(models.Model):
    name = models.CharField(max_length=50)
    educationalqualification = models.CharField(max_length=40)
    serviceduration = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    description = models.CharField(max_length=30)
    picture = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'talentteacher'


class Teacher(models.Model):
    teacherid = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=40)
    picture = models.CharField(max_length=40)
    groupp = models.CharField(max_length=30)
    academicqualification = models.CharField(max_length=40)
    trainingexprience = models.CharField(max_length=40)
    teachingarea = models.CharField(max_length=40)
    previousemployment = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=5)
    email = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30)
    paddress = models.CharField(max_length=20)
    peraddress = models.CharField(max_length=20)
    joiningdate = models.CharField(max_length=20, blank=True, null=True)
    maritalstatus = models.CharField(max_length=12)
    dateofbirth = models.DateField()

    class Meta:
        managed = False
        db_table = 'teacher'


class Teacheraccountinfo(models.Model):
    teacherid = models.CharField(max_length=10)
    paidamount = models.CharField(max_length=10)
    typeteacherid = models.IntegerField()
    dayid = models.IntegerField()
    monthid = models.IntegerField()
    yearid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teacheraccountinfo'


class Thana(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'thana'


class ThreeFourClark(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=25)
    picture = models.CharField(max_length=40)
    groupp = models.CharField(max_length=30)
    academicqualification = models.CharField(max_length=40)
    trainingexprience = models.CharField(max_length=40)
    teachingarea = models.CharField(max_length=40)
    previousemployment = models.CharField(max_length=40)
    position = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=5)
    email = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30)
    paddress = models.CharField(max_length=20)
    peraddress = models.CharField(max_length=20)
    joiningdate = models.CharField(max_length=20, blank=True, null=True)
    marid = models.CharField(max_length=5)
    day = models.CharField(max_length=4)
    month = models.CharField(max_length=15)
    year = models.CharField(max_length=8)
    type = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'three_four_clark'


class Typeteacher(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'typeteacher'


class Upcomingevent(models.Model):
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    description = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'upcomingevent'


class Usefullink(models.Model):
    name = models.CharField(max_length=25)
    link = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'usefullink'


class Village(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'village'


class Webadminlogin(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'webadminlogin'


class Year(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'year'

from django.db import models

# Create your models here.
class candidates(models.Model):
    uniqueID = models.IntegerField(unique = True,primary_key = True,)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    about = models.SlugField()
    program = models.FileField(upload_to='programs/%Y/%m/%d/'+'CppTests.cpp')
    dateTime = models.DateTimeField(auto_now_add=True)


# MODEL OF CANDIDATES PROGRAMS
def userUploadFilePath(instanse,fileName):
    '''
    instanse - model you are calling from
    filename - name of file, given in upload

    returns filepath [unix format] 
    '''
    frstName    = instanse.candidate.firstName
    lstName     = instanse.candidate.lastName
    dirName     = frstName + '_' + lstName
    fileName    = instanse.typeOfLang  
    return 'candidates/{0}/{1}'.format(dirName,filename)

class program(models.Model):
    # SOME CONSTANT DATA
    #language type of program [required for program autotesting]
    LANGUAGES = [
            ('c','C'),
            ('c++11','C++11'),
            ('c++14','C++14'),
            ('c++17','C++17'),
            ('python3','Python3'),
            ]
    #types of inputing the program
    PROGTYPES = [
            ('file','File'),
            ('text','Text'),
            ]
    #a owner model to whom the program belong
    PARENTMODEL = 'candidates'
    #MODEL FIELDS
    #uniqe id to all quizez [required for autotesting]
    quizID       = models.IntegerField(unique=True) 
    #type of program [required for this class methods]
    typeOfProg   = models.CharField(
            max_length  = 4,
            choices     = PROGTYPES,
            default     = 'file',
            )
    # lang type [required for autotests]
    typeOfLang   = models.CharField(
            max_length  = 10,
            choices     = LANGUAGES,
            default     = 'c',
            )
    progInText   = models.TextField()
    progInFile   = models.FileField(
            upload_to=userUploadFilePath,
            ) 
    candidate    = models.ForeignKey(
            PARENTMODEL,
            on_delete    = models.CASCADE,
            related_name = 'cands'
            )
    #TRUE IF PROGRAM IS WRITTEN IN TEXT AND IN FILE
    def WrittenInText(self):
        if (self.typeOfProg.field_name == 'text'):
            return True
        else:
            return False
    def WrittenInFile(self):
        if (self.typeOfProg.field_name == 'file'):
            return True
        else:
            return False
    #FUNCTION THAT MAKES FILE FROM PROGRAM IN TEXT
    def FileFromText(self):
        if (WrittenInText()):
    # CONNECTING TEXT WITH FILE
    # save = false to avoid saving while connecting (saving for save()) 
            Content = ContentFile(self.progInText)
            self.progInFile.save(
                    userUploadFilePath(),
                    Content,
                    save = False
                    )

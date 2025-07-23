from django.db import models

# Create your models here.

class Student(models.Model):
    FIRST_YEAR = 'first'
    SECOND_YEAR = 'second'
    THIRD_YEAR = 'third'
    FOURTH_YEAR= 'fourth'

    YEAR_IN_SCHOOL_CHOICES = [
        (FIRST_YEAR, 'Первый курс'),
        (SECOND_YEAR, 'Второй курс'),
        (THIRD_YEAR, 'Третий курс'),
        (FOURTH_YEAR, 'Четвертый курс'),
    ]

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    year = models.CharField(max_length=6, choices=YEAR_IN_SCHOOL_CHOICES, default=FIRST_YEAR, verbose_name='Курс')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ['last_name']


    # name = models.CharField(max_length=100)
    # group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    #
    # def __str__(self):
    #     return self.name


    # first_name = models.CharField(max_length=150, verbose_name="Имя")
    # last_name = models.CharField(max_lenght=150, verbose_name="Фамилия", unique=True)
    #
    # age = models.IntegerField(help_text='Введите возраст студента') # числовое значение
    # is_active = models.BooleanField(default=True) # булево значение
    # description = models.TextField(null=True, blank=True) # Отображение не фиксированной длины
    # created_at = models.DateTimeField(auto_now_add=True) # Отображение даты и времени создания студента,
    # # непосредственно создание записи
    # image = models.ImageField(upload_to='photos/', verbose_name='Фотография') # Для хранения изображений
    # group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='students') # ForeignKey связь один ко многим
    # profile = models.OneToOneField(Profile, on_delete=models.CASCADE) # OneToOneField связь один к одному
    # tags = models.ManyToManyField(Tag) # ManyToManyField связь многим ко многим
    #
    # STATUS_CHOICES = [
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    # ]
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    #
    #
    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
    #
    # class Meta:
    #     verbose_name = "студент"
    #     verbose_name_plural = "студенты"
    #     ordering = ["last_name"]
    #     db_table = "custom_table_name"


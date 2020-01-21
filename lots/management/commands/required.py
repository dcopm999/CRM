import factory
import random
from decimal import Decimal

factory.Faker._DEFAULT_LOCALE = 'ru_RU'


class CountryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'addresses.Country'
        django_get_or_create = ('name', )

    name = factory.Faker('country')


class RegionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'addresses.Region'
        django_get_or_create = ('name', )

    parent = CountryFactory()
    name = factory.Faker('region')

class CityFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'addresses.City'
        django_get_or_create = ('name', )

    parent = RegionFactory()
    name = factory.Faker('city')


class DistrictFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'addresses.District'
        django_get_or_create = ('name', )

    parent = CityFactory()
    name = factory.Faker('city')


class StreetFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'addresses.Street'
        django_get_or_create = ('name', )

    name = factory.Faker('street_name')
    parent = DistrictFactory()




class MakerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Maker'
        django_get_or_create = ('name', )

    name = factory.Faker('company')
    country = CountryFactory()


class TradeNameFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.TradeName'
        django_get_or_create = ('name', )

    name = factory.Faker('word')


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Category'
        django_get_or_create = ('name', )

    name = factory.Faker('word')


class MeasureFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Measure'
        django_get_or_create = ('name', )

    name = factory.Faker('pyint')


class PackingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Packing'
        django_get_or_create = ('name', )

    name = factory.Faker('word')


class OriginalFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Original'
        django_get_or_create = ('count', )

    count = factory.Faker('pyint')


class GoodFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'goods.Good'
        django_get_or_create = ('description', )

    name = TradeNameFactory()
    maker = MakerFactory()
    packing = PackingFactory()
    original = OriginalFactory()
    category = CategoryFactory()
    measure = MeasureFactory()
    description = factory.Faker('text')


class DepartmentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'hr.Department'
        django_get_or_create = ('name', )

    name = factory.Faker('job')


class EmployeeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'hr.Employee'
        django_get_or_create = (
            'first_name',
            'last_name',
            'middle_name',
            'phone',
            'position',
            'role',
            'birthday',
        )

    department = DepartmentFactory()
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    middle_name = factory.Faker('middle_name')
    phone = factory.Faker('phone_number')
    position = factory.Faker('job')
    role = factory.Faker('job')
    birthday = factory.Faker('date_of_birth')


class ContragentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'contragents.Contragent'
        django_get_or_create = (
            'name',
            'address_ur',
            'contragent_type',
            'country',
            'city',
            'district',
            'street',
            'house',
            'inn',
            'okonh',
            'okpo',
            'oked',
            'code_nds',
            'manager',
        )

    name = factory.Faker('company')
    address_ur = factory.Faker('address')
    contragent_type = random.choice([1, 2])
    country = CountryFactory()
    region = RegionFactory()
    city = CityFactory()
    district = DistrictFactory()
    street = StreetFactory()
    house = factory.Faker('pyint')
    inn = factory.Faker('credit_card_number')
    okonh = factory.Faker('word')
    okpo = factory.Faker('word')
    oked = factory.Faker('word')
    code_nds = factory.Faker('word')
    manager = EmployeeFactory()


class ContactFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'contragents.Contact'
        django_get_or_create = (
            'first_name',
            'middle_name',
            'last_name',
            'phone',
            'position',
            'role',
            'birthday',
        )

    contragent = ContragentFactory()
    first_name = factory.Faker('name')
    middle_name = factory.Faker('middle_name')
    last_name = factory.Faker('last_name')
    phone = factory.Faker('phone_number')
    position = factory.Faker('job')
    role = factory.Faker('job')
    birthday = factory.Faker('date')


class CurrencyFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'lots.Currency'
        django_get_or_create = ('name', )

    name = factory.Faker('currency_name')


class StockFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'stocks.Stock'
        django_get_or_create = (
            'name',
            'house',
            )

    name = factory.Faker('word')
    country = CountryFactory()
    house = factory.Faker('building_number')
    region = RegionFactory()
    city = CityFactory()
    district= DistrictFactory()
    street = StreetFactory()


class LotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'lots.Lot'
        django_get_or_create = (
            'base_price',
            'series',
            'shelf_life',
            'quantity',
        )

    good = GoodFactory()
    base_price = Decimal('25.00')
    series = factory.Faker('upc_e')
    currency = CurrencyFactory()
    shelf_life = factory.Faker('future_date')
    quantity = factory.Faker('pyint')
    stock = StockFactory()


class RevaluationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'revaluation.Pricing'
        django_get_or_create = ('name', 'coefficient', )

    name = factory.Faker('word')
    coefficient = factory.Faker('pyfloat')


class TaskStatusFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'crm.TaskStatus'
        django_get_or_create = ('name', )

    name = factory.Faker('word')


class AgreementFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'crm.Agreement'
        django_get_or_create = ('result', )

    result = random.choice([0,1,2])

class AgreementTaskFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'crm.AgreementTask'
        django_get_or_create = ('desc', 'date', 'is_active', )

    status = TaskStatusFactory()
    agreement = AgreementFactory()
    contact = ContactFactory()
    desc = factory.Faker('text')
    date = factory.Faker('date')
    is_active = factory.Faker('pybool')


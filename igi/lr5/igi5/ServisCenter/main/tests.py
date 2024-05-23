from django.test import TestCase, Client
from django.urls import reverse
from .models import Request
from django.db.models import Count

class RequestModelTest(TestCase):
    def setUp(self):
        # Создаем тестовые данные
        Request.objects.create(requestId=1, jobId=101)
        Request.objects.create(requestId=2, jobId=102)
        Request.objects.create(requestId=1, jobId=103)

    def test_request_count(self):
        # Проверяем количество записей в базе данных
        self.assertEqual(Request.objects.count(), 3)

    def test_most_frequent_request_id(self):
        # Проверяем самый частый requestId
        most_frequent = Request.objects.values('requestId').annotate(count=Count('requestId')).order_by('-count').first()
        self.assertEqual(most_frequent['requestId'], 1)
        self.assertEqual(most_frequent['count'], 2)

class RequestViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Создаем тестовые данные
        Request.objects.create(requestId=1, jobId=101)
        Request.objects.create(requestId=2, jobId=102)
        Request.objects.create(requestId=1, jobId=103)

    def test_most_frequent_request_id_view(self):
        response = self.client.get(reverse('most_frequent_request_id'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The most frequent request ID is: 1')
        self.assertContains(response, 'It appears 2 times.')

class RequestModelTest(TestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.request1 = Request.objects.create(requestId=1, jobId=101)
        self.request2 = Request.objects.create(requestId=2, jobId=102)
        self.request3 = Request.objects.create(requestId=1, jobId=103)

    def test_request_count(self):
        # Проверяем количество записей в базе данных
        self.assertEqual(Request.objects.count(), 3)

    def test_most_frequent_request_id(self):
        # Проверяем самый частый requestId
        most_frequent = Request.objects.values('requestId').annotate(count=Count('requestId')).order_by('-count').first()
        self.assertEqual(most_frequent['requestId'], 1)
        self.assertEqual(most_frequent['count'], 2)

    def test_create_request(self):
        # Тест на создание нового Request
        new_request = Request.objects.create(requestId=3, jobId=104)
        self.assertEqual(Request.objects.count(), 4)
        self.assertEqual(new_request.requestId, 3)
        self.assertEqual(new_request.jobId, 104)

    def test_update_request(self):
        # Тест на обновление Request
        self.request1.jobId = 105
        self.request1.save()
        self.request1.refresh_from_db()
        self.assertEqual(self.request1.jobId, 105)

    def test_delete_request(self):
        # Тест на удаление Request
        self.request2.delete()
        self.assertEqual(Request.objects.count(), 2)

class RequestViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Создаем тестовые данные
        self.request1 = Request.objects.create(requestId=1, jobId=101)
        self.request2 = Request.objects.create(requestId=2, jobId=102)
        self.request3 = Request.objects.create(requestId=1, jobId=103)

    def test_most_frequent_request_id_view(self):
        response = self.client.get(reverse('most_frequent_request_id'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The most frequent request ID is: 1')
        self.assertContains(response, 'It appears 2 times.')

    def test_template_used(self):
        response = self.client.get(reverse('most_frequent_request_id'))
        self.assertTemplateUsed(response, 'main/most_frequent_request_id.html')

    def test_context_data(self):
        response = self.client.get(reverse('most_frequent_request_id'))
        self.assertEqual(response.context['most_frequent_id'], 1)
        self.assertEqual(response.context['most_frequent_count'], 2)

class RequestCRUDTest(TestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.request1 = Request.objects.create(requestId=1, jobId=101)
        self.request2 = Request.objects.create(requestId=2, jobId=102)
        self.request3 = Request.objects.create(requestId=1, jobId=103)

    def test_create_request(self):
        # Тест на создание нового Request
        new_request = Request.objects.create(requestId=3, jobId=104)
        self.assertEqual(Request.objects.count(), 4)
        self.assertEqual(new_request.requestId, 3)
        self.assertEqual(new_request.jobId, 104)

    def test_read_request(self):
        # Тест на чтение Request
        request = Request.objects.get(requestId=1, jobId=101)
        self.assertEqual(request.jobId, 101)

    def test_update_request(self):
        # Тест на обновление Request
        self.request1.jobId = 105
        self.request1.save()
        self.request1.refresh_from_db()
        self.assertEqual(self.request1.jobId, 105)

    def test_delete_request(self):
        # Тест на удаление Request
        self.request2.delete()
        self.assertEqual(Request.objects.count(), 2)

    def test_filter_requests(self):
        # Тест на фильтрацию Request по requestId
        requests = Request.objects.filter(requestId=1)
        self.assertEqual(requests.count(), 2)
        self.assertEqual(requests.first().jobId, 101)
        self.assertEqual(requests.last().jobId, 103)

    def test_order_by_jobId(self):
        # Тест на сортировку Request по jobId
        requests = Request.objects.order_by('jobId')
        self.assertEqual(requests.first().jobId, 101)
        self.assertEqual(requests.last().jobId, 103)

class RequestViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Создаем тестовые данные
        self.request1 = Request.objects.create(requestId=1, jobId=101)
        self.request2 = Request.objects.create(requestId=2, jobId=102)
        self.request3 = Request.objects.create(requestId=1, jobId=103)

    def test_request_list_view(self):
        # Тест на получение списка Request через представление
        response = self.client.get('/requests/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Id заказа: 1')
        self.assertContains(response, 'Id заказа: 2')

    def test_request_detail_view(self):
        # Тест на получение деталей Request через представление
        response = self.client.get(f'/requests/{self.request1.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Id заказа: 1')
        self.assertContains(response, 'Id услуги: 101')

    def test_create_request_view(self):
        # Тест на создание нового Request через представление
        response = self.client.post('/requests/new/', {'requestId': 3, 'jobId': 104})
        self.assertEqual(response.status_code, 302)  # Redirect после успешного создания
        self.assertEqual(Request.objects.count(), 4)
        new_request = Request.objects.get(requestId=3)
        self.assertEqual(new_request.jobId, 104)

    def test_update_request_view(self):
        # Тест на обновление Request через представление
        response = self.client.post(f'/requests/{self.request1.id}/edit/', {'requestId': 1, 'jobId': 105})
        self.assertEqual(response.status_code, 302)  # Redirect после успешного обновления
        self.request1.refresh_from_db()
        self.assertEqual(self.request1.jobId, 105)

    def test_delete_request_view(self):
        # Тест на удаление Request через представление
        response = self.client.post(f'/requests/{self.request2.id}/delete/')
        self.assertEqual(response.status_code, 302)  # Redirect после успешного удаления
        self.assertEqual(Request.objects.count(), 2)
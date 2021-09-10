from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from tablib import Dataset

def paginasinya(object_list, page=1, limit=10, **kwargs):
	min_limit = 1
	max_limit = 10

	try:
		page = int(page)
		if page < 1:
			page = 1
	except (TypeError, ValueError):
		page=1

	try:
		limit = int(limit)
		if limit < min_limit:
			limit = min_limit
	except (ValueError, TypeError):
		limit = max_limit

	paginator = Paginator(object_list, limit)
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)

	alamat = kwargs['alamat']
	posisi = alamat.rfind("=")

	if objects.has_previous():
		alamatPrev = alamat[:posisi+1] + str(page - 1)
	else:
		alamatPrev = False

	if objects.has_next():
		alamatNext = alamat[:posisi+1] + str(page + 1)
		if posisi == -1:
			alamatNext = alamat + "?page=2"
	else:
		alamatPrev = alamat[:posisi+1] + str(paginator.num_pages - 1)
		alamatNext = False

	data = {
		'count': paginator.num_pages,
		'current': page,
		'previous_page': objects.has_previous() and objects.previous_page_number() or None, 
		'next_page': objects.has_next(),
		'previous': alamatPrev,
		'next': alamatNext,
		'total_data': len(object_list),
		'data': list(objects)
	}
	data.update(kwargs)

	return data  


def mengimport(get_formatnya, get_filenya, class_resourcenya):
	file_format = get_formatnya    # contohnya : get_formatnya = request.POST['file-format']
	databaru = get_filenya		   # contohnya : get_filenya = request.POST['file-format']t

	data_resourcenya = class_resourcenya    # contohnya class_resourcenya = DatasResource()
	dataset = Dataset()

	hasil = False
	if file_format == 'xlsx':
		imported_data = dataset.load(databaru.read() ,format='xlsx')
		result = data_resourcenya.import_data(imported_data, dry_run=True)
		# print(dataset)
		
		if not result.has_errors():
			data_resourcenya.import_data(dataset, dry_run=False)
			# print("sukses disimpan")
			hasil = True

	elif file_format == 'csv':
		imported_data = dataset.load(databaru.read().decode('utf-8'),format='csv')
		result = data_resourcenya.import_data(dataset, dry_run=True)
		
		if not result.has_errors():
			data_resourcenya.import_data(dataset, dry_run=False)
			hasil = True

	return hasil


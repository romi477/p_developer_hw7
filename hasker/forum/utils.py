from django.utils.text import slugify



def unique_slug_generator(model_inst, title):
    slug = slugify(title)
    model_class = model_inst.__class__
    
    while model_class.objects.filter(slug=slug).exists():
        obj_pk = model_class.objects.latest('pk')
        obj_pk = obj_pk.pk + 1
        
        slug = f'{slug}-{obj_pk}'
    
    return slug
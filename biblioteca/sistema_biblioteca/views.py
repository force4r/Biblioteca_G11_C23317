from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def index(request):
   print(reverse('agregar_libro'))
   print(request.method)
   context = {}

   return render(request, 'sistema_biblioteca/index.html', context)


def catalogo(request, año=0):
   print(request.method)
   if int(año) < 2015 and int(año) != 0:
      return HttpResponseNotFound("<h4>No hay datos previos al año 2015.</h4>")

   catalogo = [
      {
         'nombre_autor': 'Jorge Luis',
         'apellido_autor': 'Borges',
         'nombre_libro': 'El Aleph',
         'año_ingreso': 2015,
         'descripcion': 'La mayoría de los cuentos reunidos en este libro pertenecen al género fantástico. Algunos surgieron a partir de crónicas policiales, de pinturas o simplemente de la visión de algún conventillo; otro explora el efecto que la inmortalidad causaría en los hombres; hay una glosa al Martín Fierro, sueños sobre la identidad personal y fantasías del tiempo. El cuento El Aleph, publicado por primera vez en 1945, aborda uno de los temas recurrentes en la literatura de Borges: el infinito. Porque en esa esfera resplandeciente confluyen de un modo asombroso todos los tiempos y todos los espacios.'
      },
      {
         'nombre_autor': 'José',
         'apellido_autor': 'Hernández',
         'nombre_libro': 'Martín Fierro',
         'año_ingreso': 2022,
         'descripcion': 'José Hernández (1834-1886) fue periodista, diputado, ministro y aventurero, y está considerado como el máximo representante de la poesía gauchesca. Su poema narrativo y épico Martín Fierro dio universalidad a la figura del gaucho, que simboliza al tipo errante y desheredado, pionero en una tierra hostil. La obra, que recoge el lenguaje coloquial de sus personajes, tiene un contenido social, reivindicativo y autobiográfico y brinda no sólo un vigoroso cuadro de la pampa y sus gauchos, sino también una nítida visión de la filosofía popular. Martín Fierro es una de las obras maestras de la literatura iberoamericana.'
      },
      {
         'nombre_autor': 'Jorge Luis',
         'apellido_autor': 'Borges',
         'nombre_libro': 'El Hacedor',
         'año_ingreso': 2016,
         'descripcion': 'En «El hacedor» confluyen las simbologías de Oriente y Occidente, el cosmos y las cosmogonías, los siglos, las dinastías, lo universal y lo profundamente local: Heráclito, Homero, Dante con Rosas, Facundo y Juan Muraña. Tal diversidad de temas se corresponde con una multiplicidad de géneros.'
      },
      {
         'nombre_autor': 'Bram',
         'apellido_autor': 'Stoker',
         'nombre_libro': 'Drácula',
         'año_ingreso': 2015,
         'descripcion': 'Jonathan Harker viaja a Transilvania para cerrar un negocio inmobiliario con un misterioso conde que acaba de comprar varias propiedades en Londres; al llegar, en el Paso de Borgo un siniestro carruaje lo recoge para llevarlo, acunado por el canto de los lobos, a un castillo en ruinas. Tal es el inquietante principio de una novela magistral que alumbra uno de los personajes más populares y poderosos de todos los tiempos , pues si hay un mito literario que haya cobrado vida propia, sin duda es el del conde Drácula, el arquetipo mismo del vampiro. Publicada en 1897, y recibida como perteneciente al género gótico, sus repercusiones han desbordado con creces el ámbito cerrado del género. Así, esta novela sorprende por su solidez y arquitectura: la ausencia del erudito narrador decimonnico, sustituido por el género epistolar, y la acumulación de materiales de primera mano confieren al relato una modernidad narrativa insólita en este tipo de obras, al mismo tiempo que la lenta progresión en el desvelamiento del misterio crea una atmósfera de suspense pocas veces igualada. Claramente, Bram Stoker (1847-1912) supo sintetizar en Drácula varias de las más profundas pulsiones del ser humano .la vida, la muerte, la sexualidad. en sus más diversas y ambiguas manifestaciones .el bien y el mal, la luz y las tinieblas, la entrega no deseada pero irresistible., para alumbrar este relato fascinante que es ya un clásico indiscutible de la literatura de terror.'
      },
      {
         'nombre_autor': 'Alejandro',
         'apellido_autor': 'Dumas',
         'nombre_libro': 'El Conde de Montecristo',
         'año_ingreso': 2018,
         'descripcion': 'Edmond Dants, un joven marinero de Marsella, est a punto de convertirse en capitn de su propio barco y casarse con su am ada. Pero algunos enemigos rencorosos provocan su detencin, y lo condenan a prisin perpetua. Luego, el nico compaero de Edmond en prisin le revela su plan secreto de fuga y una car ta con instrucciones de riquezas ocultas en la isla de Monte cristo. Aquel misterioso tesoro le permitir a Edmond financi ar el sueo de crearse una nueva identidad: el enigmtico y po deroso conde de Montecristo. En esta novela, Alejandro Dumas emplea todos los elementos del drama: el suspenso, la intri ga, el amor, la venganza, la aventura apasionante y el triun fo del bien sobre el mal, que contribuyen al irresistible at ractivo de esta historia clsica y atemporal.'
      },
      {
         'nombre_autor': 'Ivo',
         'apellido_autor': 'Andric',
         'nombre_libro': 'Un Puente sobre el Drina',
         'año_ingreso': 2022,
         'descripcion': 'Una crónica de cinco siglos donde Ivo Andric, Premio Nobel de Literatura, retrata la trágica historia de los Balcanes. La ciudad de Visegrad, situada a orillas del río Drina, tuvo un momento de esplendor en la Edad Media por constituir un puente de tránsito entre el mundo cristiano y el islámico. Esta novela recoge la historia de esa comunidad plural y conflictiva, tomando como pretexto narrativo el gran puente de piedra que cruza el río, lugar de encuentro y paseo para sus habitantes. La larga crónica abarca desde el siglo XVI hasta principios del XX, y nos da cuenta de las tensiones y enfrentamientos que se suceden y heredan de generación en generación.'
      },
   ]
   context = {
      'cat_lista': catalogo,
      'año_ingreso': año
   }
   return render(request, 'sistema_biblioteca/catalogo.html', context)


def libros(request):
   catalogo = [
      {
         'nombre_autor': 'Jorge Luis',
         'apellido_autor': 'Borges',
         'nombre_libro': 'El Aleph',
         'año_ingreso': 2015,
         'descripcion': 'La mayoría de los cuentos reunidos en este libro pertenecen al género fantástico. Algunos surgieron a partir de crónicas policiales, de pinturas o simplemente de la visión de algún conventillo; otro explora el efecto que la inmortalidad causaría en los hombres; hay una glosa al Martín Fierro, sueños sobre la identidad personal y fantasías del tiempo. El cuento El Aleph, publicado por primera vez en 1945, aborda uno de los temas recurrentes en la literatura de Borges: el infinito. Porque en esa esfera resplandeciente confluyen de un modo asombroso todos los tiempos y todos los espacios.'
      },
      {
         'nombre_autor': 'José',
         'apellido_autor': 'Hernández',
         'nombre_libro': 'Martín Fierro',
         'año_ingreso': 2022,
         'descripcion': 'José Hernández (1834-1886) fue periodista, diputado, ministro y aventurero, y está considerado como el máximo representante de la poesía gauchesca. Su poema narrativo y épico Martín Fierro dio universalidad a la figura del gaucho, que simboliza al tipo errante y desheredado, pionero en una tierra hostil. La obra, que recoge el lenguaje coloquial de sus personajes, tiene un contenido social, reivindicativo y autobiográfico y brinda no sólo un vigoroso cuadro de la pampa y sus gauchos, sino también una nítida visión de la filosofía popular. Martín Fierro es una de las obras maestras de la literatura iberoamericana.'
      },
      {
         'nombre_autor': 'Jorge Luis',
         'apellido_autor': 'Borges',
         'nombre_libro': 'El Hacedor',
         'año_ingreso': 2016,
         'descripcion': 'En «El hacedor» confluyen las simbologías de Oriente y Occidente, el cosmos y las cosmogonías, los siglos, las dinastías, lo universal y lo profundamente local: Heráclito, Homero, Dante con Rosas, Facundo y Juan Muraña. Tal diversidad de temas se corresponde con una multiplicidad de géneros.'
      },
      {
         'nombre_autor': 'Bram',
         'apellido_autor': 'Stoker',
         'nombre_libro': 'Drácula',
         'año_ingreso': 2015,
         'descripcion': 'Jonathan Harker viaja a Transilvania para cerrar un negocio inmobiliario con un misterioso conde que acaba de comprar varias propiedades en Londres; al llegar, en el Paso de Borgo un siniestro carruaje lo recoge para llevarlo, acunado por el canto de los lobos, a un castillo en ruinas. Tal es el inquietante principio de una novela magistral que alumbra uno de los personajes más populares y poderosos de todos los tiempos , pues si hay un mito literario que haya cobrado vida propia, sin duda es el del conde Drácula, el arquetipo mismo del vampiro. Publicada en 1897, y recibida como perteneciente al género gótico, sus repercusiones han desbordado con creces el ámbito cerrado del género. Así, esta novela sorprende por su solidez y arquitectura: la ausencia del erudito narrador decimonnico, sustituido por el género epistolar, y la acumulación de materiales de primera mano confieren al relato una modernidad narrativa insólita en este tipo de obras, al mismo tiempo que la lenta progresión en el desvelamiento del misterio crea una atmósfera de suspense pocas veces igualada. Claramente, Bram Stoker (1847-1912) supo sintetizar en Drácula varias de las más profundas pulsiones del ser humano .la vida, la muerte, la sexualidad. en sus más diversas y ambiguas manifestaciones .el bien y el mal, la luz y las tinieblas, la entrega no deseada pero irresistible., para alumbrar este relato fascinante que es ya un clásico indiscutible de la literatura de terror.'
      },
      {
         'nombre_autor': 'Alejandro',
         'apellido_autor': 'Dumas',
         'nombre_libro': 'El Conde de Montecristo',
         'año_ingreso': 2018,
         'descripcion': 'Edmond Dants, un joven marinero de Marsella, est a punto de convertirse en capitn de su propio barco y casarse con su am ada. Pero algunos enemigos rencorosos provocan su detencin, y lo condenan a prisin perpetua. Luego, el nico compaero de Edmond en prisin le revela su plan secreto de fuga y una car ta con instrucciones de riquezas ocultas en la isla de Monte cristo. Aquel misterioso tesoro le permitir a Edmond financi ar el sueo de crearse una nueva identidad: el enigmtico y po deroso conde de Montecristo. En esta novela, Alejandro Dumas emplea todos los elementos del drama: el suspenso, la intri ga, el amor, la venganza, la aventura apasionante y el triun fo del bien sobre el mal, que contribuyen al irresistible at ractivo de esta historia clsica y atemporal.'
      },
      {
         'nombre_autor': 'Ivo',
         'apellido_autor': 'Andric',
         'nombre_libro': 'Un Puente sobre el Drina',
         'año_ingreso': 2022,
         'descripcion': 'Una crónica de cinco siglos donde Ivo Andric, Premio Nobel de Literatura, retrata la trágica historia de los Balcanes. La ciudad de Visegrad, situada a orillas del río Drina, tuvo un momento de esplendor en la Edad Media por constituir un puente de tránsito entre el mundo cristiano y el islámico. Esta novela recoge la historia de esa comunidad plural y conflictiva, tomando como pretexto narrativo el gran puente de piedra que cruza el río, lugar de encuentro y paseo para sus habitantes. La larga crónica abarca desde el siglo XVI hasta principios del XX, y nos da cuenta de las tensiones y enfrentamientos que se suceden y heredan de generación en generación.'
      },
   ]
   context = {
      'cat_lista': catalogo,
   }       
   return render(request,'sistema_biblioteca/libros.html', context)

def agregar_libro(request):
   return HttpResponse("Agregar libro")

def eliminar_libro(request):
   return HttpResponse("Eliminar libro")

def agregar_autor(request):
   return HttpResponse("Agregar autor")

def eliminar_autor(request):
   return HttpResponse("Eliminar autor")
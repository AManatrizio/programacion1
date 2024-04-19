#Renombramos la importacion para evitar conflictos
from .usuario import Usuario as UsuarioResource
from .usuario import Usuarios as UsuariosResource

from .libros import Libro as LibroResource
from .libros import Libros as LibrosResource

from .prestamo import Prestamo as PrestamoResource
from .prestamo import Prestamos as PrestamosResource

from .signin import SingIn as SignInResource

from .login import Login as LoginResource

from .notificacion import Notificaciones as NotificacionResource

from .configuracion import Configuracion as ConfiguracionResource
from .configuracion import Configuraciones as ConfiguracionesResource

from .valoraciones import Valoracion as ValoracionResource
from .valoraciones import Valoraciones as ValoracionesResource

from .comentario import Comentario as ComentarioResource
from .comentario import Comentarios as ComentariosResource


#Archivo para renombrar todos los recursos


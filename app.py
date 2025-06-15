from crud import insert_therapist
from db import close_all_connections

insert_therapist("Lucas", "William", "lucas.william123@gmail.com", "wilucas32", "Male")

close_all_connections()

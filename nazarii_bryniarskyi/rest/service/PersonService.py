import logging

from nazarii_bryniarskyi.rest.dao.PersonRepo import PersonRepo
from nazarii_bryniarskyi.rest.model.Person import Person


class PersonService:

    @staticmethod
    def findAll():
        return PersonRepo.findAll()


    @staticmethod
    def findById(id):
        return PersonRepo.findById(id)


    @staticmethod
    def save(name, surname):
        return PersonRepo.save(Person(name, surname))


    @staticmethod
    def update(id, name=None, surname=None):
        isUpdated = PersonRepo.update(id, name, surname)
        if isUpdated:
            return "Person was updated"
        return "Person was NOT updated"


    @staticmethod
    def delete(id):
        isDeleted = PersonRepo.delete(id)
        if isDeleted:
            return "Person was deleted"
        return "Person was NOT deleted"

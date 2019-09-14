
import requests

class SearchBuilder():
   __builder = None

   def setBuilder(self, builder, scraper, name):
      self.__builder = builder

   def getInformation(self, scraper, name):
      payload = Payload(scraper)
      payload.setScraper(scraper)

      # First goes the body
      information = self.__builder.getInformation()
      payload.setInformation(information)

      # Then engine
      scores = self.__builder.getScores()
      payload.setScores(scores)

      return payload


class Payload:
   def __init__(self):
      self.__information = list()
      self.__scores = list()
      self.__scraper = None

   def setScraper(self, scraper):
      self.__scraper = scraper

   def getInformation(self, scraper):
      r = requests.post(SCRAPER_FACTORY_ENDPOINT, data={'scraper': self.__scraper})
      return r, r.status_code

   def setInformation(self, information):
      self.__information = information

   def setScores(self, scores):
      self.__scores.append(scores)

   def getScores(self):
      r = requests.get(AUTOML_ENDPOINT, data = {'information': self.__information})
      return r, r.status_code

   def specification(self, scraper):
      print "scraper: %s" % self.__scraper
      print "scores: %d" % self.__scores
      print "information: %s\'" % self.__information

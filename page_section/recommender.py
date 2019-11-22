# this script assumes Python 3+

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from .lista_atividades import ListaAtividades


def PAGe_Cartesian(o):
  PAGe_Axes = [
    ('Cardiovascular',  0),
    ('Nutrition',      30),
    ('Functional',     60),
    ('Sensorial',      90),
    ('Falls',         120),
    ('Violence',      150),
    ('Environment',   180),
    ('SocialSupport', 210),
    ('Cognition',     240),
    ('Depression',    270),
    ('Attitude',      300),
    ('Prescriptions', 330)
  ]
    # converts a dictionary dict[PAGe key] -> PAGe value to a list of coordinates in the Cartesian plan
  PAGe_Theta = [(axis, np.pi * angle / 180) for (axis, angle) in PAGe_Axes]
  L = []
  for (axis, theta) in PAGe_Theta:
    r = o[axis] / 100      # scales the score of the current dimension to the [0, 1] interval
    x = r * np.cos(theta)  # computes the x-coordinate in the Cartesian projection
    y = r * np.sin(theta)  # computes the y-coordinate in the Cartesian projection
    L.append((x, y))

  return L


class Recommender:
  """ Prototype 01 - Offering Scorer
      This prototype implements a demand-offer matching using a pair of fuzzy/defuzzyfication methods
      This model has 0 parameters and 1 hyperparameter (threshold)
      Predictor is a fuzzy model that computes the difference between the area of a polygon representing
         an offering and an area representing the pacient's health care demand.
      Reference: xxx ??? original contribution ???
  """

  def __init__(self, offerings, threshold):
    # offerings is a list of active offers;
    # an offer  is a dictionary that conforms to dict[PAGe key] -> PAGe value
    # threshold is the minimum match required from an offer so that it can be recommended

    # unpacks parameters
    self.offerings  = offerings
    self.threshold  = threshold

    # visits each offer and computes its 12-gon representation
    self.normaliser = 0.03 # largest difference between two 12-gons in this scenario, then scaled to 100
    self.polygons = {}
    for offer in offerings:
      self.polygons[offer['OfferID']] = Polygon(PAGe_Cartesian(offer))

    # sets class attributes
    self.desc = 'Model P01 (fuzzy scorer)'
    self.file = 'model_p01'

  def predict(self, patient, _offer):
    # patient is a dictionary that conforms to dict[PAGe key] -> PAGe value
    # _offer  is a dictionary that conforms to dict[PAGe key] -> PAGe value

    # creates 12-gon representations of offer and demand and computes the coverage
    demand    = Polygon(PAGe_Cartesian(patient))
    offer     = self.polygons[_offer['OfferID']]
    coverage  = (offer.area - offer.intersection(demand).area) / self.normaliser

    return coverage

  def scorer(self, patient):
    # patient is a dictionary that conforms to dict[PAGe key] -> PAGe value
    # returns a list of tuples that conform to (offerID, matching score) in descending order of matching scores

    L = []
    for _offer in self.offerings:
      coverage = self.predict(patient, _offer)
      if(coverage >= self.threshold):
        L.append((_offer['OfferID'], coverage))

    res = sorted(L, key = lambda e: -e[1])

    return res


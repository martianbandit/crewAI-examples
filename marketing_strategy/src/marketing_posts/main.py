#!/usr/bin/env python
import sys
from marketing_posts.crew import MarketingPostsCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'customer_domain': 'lechienvoyageur.com',
        'project_description': """
lechienvoyageur.com es une boutique de E-commerce se sp/cialisant dans les produits de transports, de voyage, et camping pour votre chien et recherche constament des produits innovateur, 
pratiques et durable et recherche dans le Pays France les tendances en terme de produits et de promotions et strategie marketing

Customer Domain: e-commerce, boutique en ligne
Project Overview: Mettre en place une solution automatisée permettant d’identifier et de rechercher des produits tendance, innovants et durables à partir d’un ensemble de plateformes et d’outils (pytrends, serper, etc.) dans le marché français.
"""
    }
    MarketingPostsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'customer_domain': 'lechienvoyageur.com',
        'project_description': """
lechienvoyageur.com es une boutique de E-commerce se sp/cialisant dans les produits de transports, de voyage, et camping pour votre chien et recherche constament des produits innovateur, 
pratiques et durable et recherche dans le Pays France les tendances en terme de produits et de promotions et strategie marketing

Customer Domain: e-commerce, boutique en ligne
Project Overview: Mettre en place une solution automatisée permettant d’identifier et de rechercher des produits tendance, innovants et durables à partir d’un ensemble de plateformes et d’outils (pytrends, serper, etc.) dans le marché français.
"""
    }
    try:
        MarketingPostsCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

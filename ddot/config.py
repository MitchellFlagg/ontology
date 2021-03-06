from __future__ import absolute_import

import ddot
import os, inspect
from ndex.networkn import NdexGraph

ndex_server = 'http://test.ndexbio.org'
ndex_user = 'scratch'
ndex_pass = 'scratch'

#########################
# Read CX Visual styles #
#########################

top_level = os.path.dirname(os.path.abspath(inspect.getfile(ddot)))
import json
with open(os.path.join(top_level, 'ontology_style.cx')) as f:
    ontology_style = NdexGraph(json.load(f))

with open(os.path.join(top_level, 'passthrough_style.cx')) as f:
    passthrough_style = NdexGraph(json.load(f))

##################################
# NDEx URLs for example networks #
##################################

GO_HUMAN_URL = 'http://dev2.ndexbio.org/v2/network/3030845c-00d5-11e8-bd69-0660b7976219'
PHAROS_URL = 'http://dev2.ndexbio.org/v2/network/a94f1c0f-789a-11e7-a1d1-0660b7976219'
MONARCH_DISEASE_GENE_URL = 'http://dev2.ndexbio.org/v2/network/07749a5f-7956-11e7-a1d1-0660b7976219'

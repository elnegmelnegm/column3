import streamlit as st
from PIL import Image
image_path = 'https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png'


import streamlit as st
import plotly.express as px
import pandas as pd
st.image(image_path)
# Complete data
data = {
    'Column': ["Zorbax Extend C18", "Capcell C18 ACR", "SepaxGP-C18", "Zorbax Eclipse XDB C18", "Monitor C18",
               "Genesis C18", "Discovery HS C18", "PurospherSTAR RP-18e 5 µm", "Genesis C18 AQ", "Prestige C18",
               "SepaxHP-C18", "Ascentis C18", "Acclaim 120 C18", "PurospherSTAR RP-18e 3 µm", "TSKgel ODS-100S",
               "Delta-Pak C18 100A", "Symmetry C18", "Luna 5 µ C18(2)", "Ultra", "BETASIL C18", "SiliaChrom XDB C18",
               "Matrix C18", "Cosmosil 5C18-AR-II", "ProntoSil 120-5-C18-H", "ProntoSil 120-5-C18-AQ Plus",
               "Pinnacle DB", "Jsphere H80", "ProntoSil 120-5-C18-SH", "Superiorex", "Prevail Select C18", "Viva 300",
               "Capcell C18 MG", "Cosmosil 5C18-MS-II", "YMC ODS-AM", "Hypersil BDS 18", "ProntoSil 120-5-C18-ace-EPS",
               "HyPurity C18", "SymmetryShield RP18", "Denali C18", "Capcell C18 MGII", "YMC ODS-A", "Xbridge C18",
               "Zorbax Rx C18", "Acquity UPLC BEH C18", "Allure", "Shim-pack XR-ODS", "YMC Pro C18 RS", "Orosil C18",
               "Xbridge Shield RP18", "Acquity UPLC BEH Shield RP18", "TSKgel ODS-100Z", "Capcell C18 UG 80",
               "YMC Pro C18", "Reliachrom C18", "Capcell C18 UG 120", "SiliaChrom XT C18", "Shim-pack VP-ODS",
               "Acclaim 120 C8", "YMC ODS-AL", "TSKgel Octyl-80Ts", "Alltima C18", "Bio Basic 18", "Acclaim Polar Advantage",
               "YMC ODS-AQ", "Discovery C18", "ProntoSil 200-5-C18-H", "TSKgel ODS-80Ts", "ProntoSil 200-5-C18-ace-EPS",
               "Chromolith Perf RP-18e", "Everest C18 300A", "Capcell C18 AG 120", "Hypersil PAH", "ProntoSil 120-5-C18-AQ",
               "Hypersil ODS-2", "Alltima HP C18", "Capcell C18 SG 120", "Pinnacle II", "Discovery C18 WP",
               "TSKgel Super-ODS", "Hypersil ODS", "Alltima C18 WP", "Zorbax StableBond C18", "BetaMax Neutral",
               "Alltima HP C18 Amide", "ProntoSil 60-5-C18-H", "ProntoSil 300-5-C18-ace-EPS", "SiliaChrom SB C18",
               "ProntoSil 300-5-C18-H", "Acclaim 300 C18", "Xterra MS C18", "Alltima HP C18 High load",
               "Shim-pack XR-ODS II", "TSKgel ODS-120A", "TSKgel ODS-100V 5 μm", "SiliaChrom AQ C18", "Hydrosphere C18",
               "TSKgel ODS-100V 3 μm", "TSKgel ODS-80TM", "Xterra RP18", "TSKgel Super-Phenyl", "SiliaChrom dt C18",
               "Purospher RP-18 endcapped", "Prevail C18", "SiliaChrom XDB2 C18", "Atlantis dC18", "ProntoSil 200-5-C18-AQ",
               "Capcell C18 AQ", "Cosmosil 5C18-PAQ", "Purospher RP-18", "SiliaChrom XDB1 C18", "TSKgel ODS-120T",
               "Jsphere M80", "Aquasil C18", "TSKgel Super-Octyl", "Alltima HP C18 AQ", "Jsphere L80", "Alltima HP C18 EPS",
               "Platinum EPS C18", "BetaBasic 18", "Supelcosil LC18", "Reliasil C18", "MicroBondapak C18", "Nova-Pak C18",
               "Superspher 100 RP-18 endcapped"],
    'Prin1': [-2.148996991, -1.610939802, -1.462305548, -2.030175195, -1.312132388, -1.602679708, -1.899563606,
              -1.339352055, -1.717488468, -1.194399857, -1.311474993, -1.779527591, -1.351595892, -1.368346631,
              -1.180792714, -0.996461022, -1.052556458, -1.4631389, -1.099599346, -1.331585751, -1.113029045,
              -1.108460658, -1.006848427, -1.108351256, -0.555404252, -0.830469371, -1.018562266, -0.585986091,
              -0.550377051, -1.274325605, -1.143321553, -0.935310009, -0.872351846, -0.479893215, -0.698602946,
              -0.836741796, -0.762497887, -0.947946521, -0.834727356, -0.879557496, -0.363147532, -0.960936321,
              0.000457702, -0.960936321, -0.256795759, -0.635833185, -1.021125641, -0.674568622, -0.789245425,
              -0.789245425, -0.72125679, 0.251305766, -0.395337711, -0.100831515, -0.357882864, -0.265937873,
              -0.321901653, -0.646203577, 0.122261162, -0.004321323, -0.461390534, -0.946085252, -0.214483914,
              0.215148446, -0.51891771, -0.089351237, -0.650412339, -0.18348987, -0.680487261, 0.701424708,
              -0.416576522, 0.04710728, 0.6783647, -0.261548699, 0.138676591, 0.550700567, -0.718680896,
              0.674480534, 0.84532381, -0.73968816, 0.200190264, -0.396426756, -0.16807337, 0.120214271,
              -0.248241762, 0.710248437, 0.24109454, -0.395065662, 0.022743066, -0.3505613, 0.983541633,
              1.306824998, 0.29858741, 0.885666306, 0.527079499, 0.331343397, 1.710307656, 0.24725376,
              0.356075438, 1.046650362, 0.366664612, 0.515627, 1.055411125, 0.780264723, 1.10925951,
              1.052346993, 1.000667416, 0.907144726, 1.045855049, 2.216335797, 1.251174322, 1.634606527,
              1.193739851, 2.197715941, 1.779726244, 2.634591822, 3.614291274, 3.856572608, 5.309679572,
              5.361618322, 4.892665187, 5.36516526],
    'Prin2': [0.626657136, 1.077198945, 0.860370528, 0.381349879, 0.088940351, -0.362529862, 0.211020641, 0.859631242,
              -0.283690977, 0.376692861, 0.147283165, 0.617706734, 0.217771166, 0.027304055, 0.313200535,
              -0.996461022, 0.031429369, 0.038251873, -0.00676842, -0.194837833, 1.346077593, -0.966411708,
              0.676759519, 1.709388236, 0.336179592, 1.656832772, -0.728330793, 1.771256106, 0.87800073,
              1.140906592, -0.382406759, -1.026785799, 0.483499458, -0.175868444, -0.125041136, -0.819981739,
              -0.332621246, -1.004880391, -0.910152831, -0.682782924, 0.4036775, -0.139831798, -0.793122853,
              1.019045125, -0.793122853, 0.696520935, -0.066828278, 1.358034202, 0.959622931, -1.32042066,
              -1.32042066, 1.060854511, 1.434710203, -0.258869857, -0.894551706, -0.331780083, 0.885943943,
              0.125218463, -1.452485961, 1.107295022, -1.09614756, 2.519439187, -1.662472966, -0.912069981,
              0.079875088, -1.35655353, -1.279168667, 0.420998187, -1.519708645, -1.457345259, -1.642255164,
              1.117281428, 0.096254725, 0.25976881, -1.981451147, -0.917822654, 1.527591421, -0.190806688,
              -0.646612014, -1.866666633, -0.88049452, -0.617159631, -0.562382918, 0.30557053, 2.956158577,
              -1.531167934, 2.969223253, -1.95525046, -1.043362994, -1.708233971, -1.981451147, -0.917822654,
              1.527591421, -0.190806688, -0.646612014, -1.866666633, -0.88049452, -0.617159631, -0.562382918,
              0.30557053, 2.956158577, -1.531167934, 2.969223253, -1.95525046, -1.043362994, -1.708233971,
              1.283919264, -0.380455051, 2.186163894, -2.209399362, 3.977174749, -1.339012013, -1.203437575,
              0.00716869, -0.954103876, 0.317837668, 1.230016956, -0.69393379, -0.984178212, 0.082257974]
}

df = pd.DataFrame(data)

# Streamlit app
st.title("Scatter Plot with Plotly and Streamlit")
st.write("Hover over points to see labels.")

fig = px.scatter(df, x='Prin1', y='Prin2', text='Column', labels={'Prin1': 'Principal Component 1', 'Prin2': 'Principal Component 2'})

fig.update_traces(marker=dict(size=12))

st.plotly_chart(fig)

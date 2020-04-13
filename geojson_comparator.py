"""
Made with love by Rovegrod 

Compare two GeoJSON files and calculate absolute and relative
error by axis 
"""
import sys
import json
import  numpy as np
import logging
import kml2geojson

def geo_comparator(path_originalfile,path_file2check):
    try:
        with open(path_originalfile) as json_file:
            origin = json.load(json_file)
    except FileNotFoundError:
        logging.error("The original file you specify was not found in the directory")
    except Exception:
        logging.error(f"Something has gone wrong reading your file -> {e}")
   
    try:
        with open(path_file2check) as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        logging.error("The file to be checked that you specify was not found in the directory")
    except Exception as e:
        logging.error(f"Something has gone wrong reading your file -> {e}")
    
    origin_coords = origin["features"][0]["geometry"]["coordinates"]
    data_coords = data["features"][0]["geometry"]["coordinates"]
    
    sum_origin = np.sum(origin_coords, axis=0)
    sum_data = np.sum(data_coords, axis=0)

    absolute_error = abs(sum(np.subtract(origin_coords, data_coords)))
    relative_error = np.divide(absolute_error, sum_origin) * 100

    logging.info(f"Sum origin: {sum_origin}")
    logging.info(f"Sum input: {sum_data}")
    logging.info(f"Absolute error by axis: {absolute_error}")
    logging.info(f"Relative error by axis: {relative_error}%")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    origin_file = str(sys.argv[1])
    file2compare = str(sys.argv[2])

    geo_comparator(origin_file, file2compare)
    
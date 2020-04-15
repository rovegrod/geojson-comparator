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
    
    lister = lambda l: [coord for point in l for coord in point]
    origin_list = lister(origin_coords)
    data_list = lister(data_coords)
    
    for point in data_coords:
        absolute_axis_error = np.sum(abs(np.subtract(origin_coords, data_coords)), axis=0)

    origin_sum = np.sum(origin_coords, axis=0)
    data_sum = np.sum(data_coords, axis=0)
    
    relative_axis_error = np.divide(absolute_axis_error, origin_sum) * 100
    absolute_mean_error_axis = np.divide(absolute_axis_error, len(origin_coords))
    
    absolute_error = sum(abs(np.subtract(origin_list, data_list)))
    relative_error = (absolute_error / np.sum(origin_list)) * 100
    absolute_mean_error = absolute_error / len(origin_list)

    logging.info(f"Absolute error by axis: {absolute_axis_error}")
    logging.info(f"Mean absolute error by axis: {absolute_mean_error_axis}")
    logging.info(f"Relative error by axis: {relative_axis_error}%\n")
    logging.info(f"Absolute error: {absolute_error}")
    logging.info(f"Mean absolute error: {absolute_mean_error}")
    logging.info(f"Relative error: {relative_error}%")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    origin_file = str(sys.argv[1])
    file2compare = str(sys.argv[2])

    geo_comparator(origin_file, file2compare)
    
import kml2geojson
import logging, sys

def conversion(kml_path, geojson_path) -> any:
    return kml2geojson.main.convert(kml_path, geojson_path)

     
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    kml_path = str(sys.argv[1])
    geojson_path = str(sys.argv[2])
    try: 
        conversion(kml_path, geojson_path)
        logging.info("SUCCESS")
    except Exception as e:
        logging.error(f"Something has gone wrong -> {e}")
    

if __name__ == '__main__':  # noqa

    import sys
    sys.path.append('C:/personal/satalite-image-water-body-finder/data_processing/rfc_processing')  # noqa

    import os
    import multiprocessing as mp
    from create_training_set_full import create_training_set
    from pathlib import Path
    import pickle

    # define parameters
    image_data_directory = Path(
        "D:/WaterBodyExtraction/WaterPolyData/image_data")
    geo_data_directory = Path(
        "D:/WaterBodyExtraction/WaterPolyData/geo_data/v2")
    label_data_directory = Path(
        "D:/WaterBodyExtraction/WaterPolyData/label_data")

    training_output_directory = Path(
        "D:/WaterBodyExtraction/WaterPolyData/training_sets/training_set_8")
    visualisation_output_directory = Path(
        "D:/WaterBodyExtraction/WaterPolyData/visualisations/training_set_8")

    pool = mp.Pool(mp.cpu_count())

    filenames = os.listdir(geo_data_directory)
    print(len(filenames))

    results = []
    length = len(filenames)

    def collect_result(result):
        global results
        results.append(result)
        print("{0} files of {1} complete".format(len(results), length))

    for filename in filenames:
        pool.apply_async(create_training_set, args=(
            filename.replace(".tif", ""), image_data_directory, label_data_directory, training_output_directory, visualisation_output_directory), callback=collect_result)

    pool.close()
    pool.join()

    print(results)
    print("Completed")
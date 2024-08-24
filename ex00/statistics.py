import numpy as np

def ft_statistics(*args, **kwargs):
    if not args:
        # Imprimir ERROR si no hay datos numéricos
        print("ERROR")
        return

    # Diccionario para almacenar los resultados de estadísticas
    results = {}
    
    # Verificar las estadísticas solicitadas en kwargs
    if "mean" in kwargs.values():
        results["mean"] = float(np.mean(args))
    if "median" in kwargs.values():
        results["median"] = float(np.median(args))
    if "quartile" in kwargs.values():
        quartile_25 = float(np.percentile(args, 25))
        quartile_75 = float(np.percentile(args, 75))
        results["quartile"] = [quartile_25, quartile_75]
    if "std" in kwargs.values():
        results["std"] = float(np.std(args))
    if "var" in kwargs.values():
        results["var"] = float(np.var(args))

    # Imprimir los resultados en el formato solicitado
    printed_result = False  # Bandera para rastrear si se imprimieron resultados válidos
    for key in ["mean", "median", "quartile", "std", "var"]:
        if key in results:
            print(f"{key} : {results[key]}")
            printed_result = True
    
    # Imprimir "ERROR" para cada estadística solicitada que no se haya calculado
    requested_stats = set(kwargs.values())
    valid_stats = {"mean", "median", "quartile", "std", "var"}
    invalid_stats = requested_stats - valid_stats

    # Asegúrate de que los errores se impriman al final y sin líneas separadoras adicionales
    if invalid_stats:
        for _ in invalid_stats:
            print("ERROR")

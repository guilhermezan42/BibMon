import unittest
from bibmon._load_data import load_nasa_pcoe_dataset

class TestLoadNASAData(unittest.TestCase):
    def test_not_implemented(self):
        """Deve levantar NotImplementedError se nenhum argumento for passado."""
        with self.assertRaises(NotImplementedError):
            load_nasa_pcoe_dataset()
    
    def test_load_from_env(self):
        """Deve carregar um CSV válido a partir da variável de ambiente."""
        import tempfile
        import pandas as pd
        import os

        df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".csv") as f:
            df.to_csv(f.name, index=False)
            os.environ["NASA_PCOE_PATH"] = f.name

        loaded = load_nasa_pcoe_dataset(use_env=True)
        self.assertIsInstance(loaded, pd.DataFrame)
        self.assertEqual(list(loaded.columns), ['a', 'b'])
    
    def test_load_from_download(self):
        """Deve baixar o CSV e carregar como DataFrame."""
        import tempfile
        import pandas as pd
        from pathlib import Path

        cache_dir = tempfile.mkdtemp()
        path = Path(cache_dir) / "bearing_dataset.csv"
        df = pd.DataFrame({'x': [10], 'y': [20]})
        df.to_csv(path, index=False)

        result = load_nasa_pcoe_dataset(download=True, cache_dir=cache_dir)
        self.assertEqual(list(result.columns), ['x', 'y'])
    
    def test_download_without_cache_dir(self):
        """Deve levantar erro se download=True sem cache_dir."""
        with self.assertRaises(ValueError):
            load_nasa_pcoe_dataset(download=True)
    


    
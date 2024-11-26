import pytest
from unittest.mock import patch, mock_open
from io import StringIO
from texhelper.bibtex import beautify_bibtex_file

# 模拟输入的 bibtex 内容
@pytest.fixture
def mock_bibtex_content():
    return """
    @article{zhang2021joint,
      title={Joint optimization of cooperative edge caching and radio resource allocation in 5G-enabled massive IoT networks},
      author={Zhang, Fan and Han, Guangjie and Liu, Li and Mart{\'\i}nez-Garc{\'\i}a, Miguel and Peng, Yan},
      journal={IEEE Internet of Things journal},
      volume={8},
      number={18},
      pages={14156--14170},
      year={2021},
      publisher={IEEE}
    }
    @article{han2021anomaly,
      title={Anomaly detection based on multidimensional data processing for protecting vital devices in 6G-enabled massive IIoT},
      author={Han, Guangjie and Tu, Juntao and Liu, Li and Mart{\'\i}nez-Garc{\'\i}a, Miguel and Peng, Yan},
      journal={IEEE Internet of Things Journal},
      volume={8},
      number={7},
      pages={5219--5229},
      year={2021},
      publisher={IEEE}
    }
    """

# 测试 beautify_bibtex_file：模拟文件读写
def test_beautify_bibtex_file(mock_bibtex_content):
    # 使用 mock_open 模拟文件读取和写入
    with patch("builtins.open", mock_open(read_data=mock_bibtex_content)) as mock_file:
        # 调用 beautify_bibtex_file，模拟从 input.bib 读取和写入 output.bib
        beautify_bibtex_file("input.bib", "output.bib")
        
        # 获取文件内容
        written_content = mock_file().getvalue()
        
        # 验证文件内容格式化是否正确
        assert "@article{zhang2021joint," in written_content
        assert "title={Joint optimization of cooperative edge caching and radio resource allocation in 5G-enabled massive IoT networks}" in written_content
        assert "author={Zhang, Fan and Han, Guangjie and Liu, Li and Mart{\'\i}nez-Garc{\'\i}a, Miguel and Peng, Yan}" in written_content
        assert "year={2021}" in written_content
        assert "@article{han2021anomaly," in written_content

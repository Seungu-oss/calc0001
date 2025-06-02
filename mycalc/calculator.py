{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOse401ainRj9Tw6Ln9lIeS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Seungu-oss/calc0001/blob/main/mycalc/calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "39Vb0xnVRvZg",
        "outputId": "01f569d8-aec9-4ceb-f112-1afedc95d695"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting mycalc/calculator.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile mycalc/calculator.py\n",
        "def add(a,b):\n",
        "    return a+b\n",
        "\n",
        "def subtract(a,b):\n",
        "    return a-b\n",
        "\n",
        "def multiply(a,b):\n",
        "    return a*b\n",
        "\n",
        "def divide(a,b):\n",
        "    return a/b"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile setup.py\n",
        "import setuptools\n",
        "\n",
        "setuptools.setup(\n",
        "    name = 'mcalcu',\n",
        "    version='0.0.1',\n",
        "    description='nice calculator',\n",
        "    author='seungu',\n",
        "    url='https://github.com/Seungu-oss/calc0001'\n",
        "    download_url='https://github.com/Seungu-oss/calc0001',\n",
        "    packages= ['mycalc'],\n",
        "    classifiers=[\n",
        "      \"Programming Language :: Python :: 3\"\n",
        "    ]\n",
        ")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0Clgq9P9VJje",
        "outputId": "e86fe453-e1ee-43b5-f989-1a77fc1ffa4a"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting setup.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git init"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6ek-n7kDbTsN",
        "outputId": "1d40e83a-757a-49e9-cd67-92b7af70b983"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[33mhint: Using 'master' as the name for the initial branch. This default branch name\u001b[m\n",
            "\u001b[33mhint: is subject to change. To configure the initial branch name to use in all\u001b[m\n",
            "\u001b[33mhint: of your new repositories, which will suppress this warning, call:\u001b[m\n",
            "\u001b[33mhint: \u001b[m\n",
            "\u001b[33mhint: \tgit config --global init.defaultBranch <name>\u001b[m\n",
            "\u001b[33mhint: \u001b[m\n",
            "\u001b[33mhint: Names commonly chosen instead of 'master' are 'main', 'trunk' and\u001b[m\n",
            "\u001b[33mhint: 'development'. The just-created branch can be renamed via this command:\u001b[m\n",
            "\u001b[33mhint: \u001b[m\n",
            "\u001b[33mhint: \tgit branch -m <name>\u001b[m\n",
            "Initialized empty Git repository in /content/.git/\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone"
      ],
      "metadata": {
        "id": "zIcWyX8qbu5P"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
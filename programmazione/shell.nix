{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.venvShellHook
    # Add any non-Python native system dependencies here (e.g., pkgs.stdenv.cc.cc.lib)
    python3Packages.jupyter
    python3Packages.notebook
    python3Packages.ipykernel
    python3Packages.numpy
    python3Packages.pandas
    python3Packages.matplotlib
    python3Packages.scikit-learn
    python3Packages.seaborn
    python3Packages.biopython
  ];

  # This automatically creates a writeable .venv folder when the shell loads
  venvDir = "./.venv";

  postShellHook = ''
    echo "Python environment initialized!"
  '';
}


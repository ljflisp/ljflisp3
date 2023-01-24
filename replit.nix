{ pkgs }: {
  deps = [
   # pkgs.replit害群之马           
                                       
                                                                               pkgs.vimHugeX
                                                                                                                                                               pkgs.rakudo
                                                                                                                                                  pkgs.nodejs-16_x
                                                                                                                                                               pkgs.lua
                                                                               pkgs.gnumake
    pkgs.dotnet-sdk  
    pkgs.haskellPackages.yabi           
    pkgs.tcl
    pkgs.julia-bin
    pkgs.ruby
    pkgs.bat
    pkgs.python3
    pkgs.crystal
    pkgs.elixir
    pkgs.go
    pkgs.replitPackages.replbox
    pkgs.graalvm17-ce
    pkgs.haskellPackages.yabi
    pkgs.fpc
    pkgs.gcc
		pkgs.nim-unwrapped
		pkgs.nimble-unwrapped
    pkgs.gforth
    pkgs.guile_3_0
    pkgs.gnuapl
    pkgs.replitPackages.basil
    
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python310}/bin/python3.10";
    LANG = "en_US.UTF-8";
  };
}


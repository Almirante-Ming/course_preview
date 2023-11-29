#! /etc/bin/env ruby

def calc_pitch(f, f0=1, p0=1)
  p=p0+12*Math.log2(f/f0)
  return p
end

What this program does:
- The main question is whether a KNOT will hold a load (will it slip or not?).

- A real knot has complicated geometry: the rope crosses over itself, there are multiple
  contact points, different contact angles and varying normal forces.

- Instead of modeling the full knot geometry directly, we simplify the friction effect
  using the idea of an "equivalent wrap":
      knot ≈ a rope wrapped around a cylinder/post for 'wraps' turns
  Here, 'wraps' is a simplified parameter that stands in for the detailed knot structure.

- The program first computes the tension produced by the hanging mass:
      T_load = m * g

- Then, using the static capstan equation, it computes the maximum load-side tension
  that can be balanced by a given holding-side tension T_hold, with friction coefficient
  mu and total contact angle theta:
      T_max = T_hold * exp(mu * theta),   where   theta = 2*pi*wraps

- Finally, it makes a decision:
      If T_load <= T_max: the knot HOLDS (in this simplified model).
      If T_load >  T_max: the knot does not hold; slipping is expected in this model.

- The program can also plot how T_max grows as the number of wraps increases.

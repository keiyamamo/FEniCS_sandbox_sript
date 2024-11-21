import dolfin

mesh = dolfin.UnitSquareMesh(10, 10)
n = dolfin.FacetNormal(mesh)

V = dolfin.VectorFunctionSpace(mesh, "DG", 2)
u = dolfin.TrialFunction(V)
v = dolfin.TestFunction(V)
a = dolfin.Constant(0)*dolfin.inner(u, v)*dolfin.dx+ dolfin.inner(u, v)*dolfin.ds
I = dolfin.Identity(len(u))
u = dolfin.Function(V, name="u")
u.interpolate(dolfin.Expression(("x[0]","sin(x[0])"), degree=1))
F = I+dolfin.grad(u)
J = dolfin.det(F)
n_new = J*dolfin.inv(F.T)*n
L = dolfin.inner(n_new, v)*dolfin.ds

A = dolfin.assemble(a, keep_diagonal=True)
A.ident_zeros()
b = dolfin.assemble(L)
nh = dolfin.Function(V, name="n")
dolfin.solve(A, nh.vector(), b)

with dolfin.XDMFFile("n_deformed.xdmf") as xdmf:
    dolfin.ALE.move(mesh, u)
    xdmf.write_checkpoint(u, "u", 0.0, append=False)
    xdmf.write_checkpoint(nh, "nh", 0.0, append=True)
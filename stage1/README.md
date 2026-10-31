# Stage 1: Identity & Access

Set up sign-in and data isolation for a Supabase app (`icor-app`). Done in the Supabase and Google Cloud consoles, so there's no code here.

## What I did
- Created a Google Cloud OAuth client and enabled "Sign in with Google" (OIDC) in Supabase.
- Created a `tasks` table with row-level security (RLS) and a policy `user_id = auth.uid()`, so each user can read only their own rows.

## Design notes
- OIDC means Google checks the password and the app only gets a signed token, so a breach of the app leaks no passwords.
- RLS enforces isolation in the database itself, not just in app code.
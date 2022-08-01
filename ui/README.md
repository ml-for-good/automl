# AutoML UI

You need to install [pnpm][1] first

```bash
$ npm i -g pnpm
```

### Install

```bash
$ pnpm i
```

### Start

```bash
$ npm run dev
```

## Project structure

```
src/
 |__features/
 |   |__<entity>/
 |       |__<entity>.api.ts
 |       |__<entity>.types.ts
 |       |__<entity>.helper.ts
 |       |__<entity>.service.ts
 |       |__<entity>.hooks.ts
 |       |__<entity>.components/
 |           |_<Components associated with this entity>
 |__layouts/
 |__pages/
 |   |__app/
 |       |__<Business pages>
 |   |__login.tsx
 |   |__register.tsx
 |__utilites
```

[1]: https://pnpm.io/

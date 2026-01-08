# 引入其他文件夹到 AstroPaper 项目

## 项目当前配置

从 `tsconfig.json` 和 `astro.config.ts` 可以看到，项目已经配置了以下路径解析规则：

- **路径别名**：`@/*` 指向 `./src/*`
- **基础路径**：`baseUrl` 设为项目根目录 `.`
- **构建工具**：使用 Vite 作为构建工具

## 引入项目内部文件夹

### 1. 使用相对路径

对于项目内部的文件夹，可以直接使用相对路径引入：

```typescript
// 引入同级文件夹
import { someFunction } from './sibling-folder/utils';

// 引入父级文件夹
import { anotherFunction } from '../parent-folder/utils';

// 引入多级父级文件夹
import { thirdFunction } from '../../../../deep-folder/utils';
```

### 2. 使用绝对路径

基于 `baseUrl` 配置，可以使用绝对路径引入：

```typescript
// 引入项目根目录下的文件夹
import { someFunction } from '/root-folder/utils';

// 引入 src 目录下的文件夹（使用内置别名）
import { anotherFunction } from '@/components/Button';
```

### 3. 扩展路径别名

如果需要为其他文件夹添加别名，可以修改 `tsconfig.json` 和 `astro.config.ts`：

#### 修改 tsconfig.json

```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"],
      "@components/*": ["./src/components/*"],
      "@utils/*": ["./src/utils/*"],
      "@external/*": ["./external-folder/*"] // 添加外部文件夹别名
    }
  }
}
```

#### 修改 astro.config.ts

```typescript
export default defineConfig({
  vite: {
    resolve: {
      alias: {
        '@external/': new URL('./external-folder/', import.meta.url).pathname,
      },
    },
  },
});
```

## 引入项目外部文件夹

### 1. 使用相对路径

对于项目外部的文件夹，可以使用相对路径引入：

```typescript
// 引入项目外部的文件夹
import { externalFunction } from '../../../external-project/utils';
```

### 2. 使用 Vite 别名

如上所述，可以通过配置 Vite 别名来引入外部文件夹。

### 3. 注意事项

- **Vite 安全限制**：默认情况下，Vite 只允许访问项目根目录内的文件
- **类型安全**：确保外部文件夹的 TypeScript 类型能被正确识别
- **构建性能**：引入过多外部文件可能影响构建速度
- **依赖管理**：确保外部文件夹的依赖与当前项目兼容

## 示例：引入其他项目的组件

假设你有一个外部项目 `../my-components`，包含一些可复用组件：

1. **配置别名**：
   ```typescript
   // astro.config.ts
   export default defineConfig({
     vite: {
       resolve: {
         alias: {
           '@my-components/': new URL('../my-components/', import.meta.url).pathname,
         },
       },
     },
   });
   ```

2. **使用别名引入**：
   ```astro
   ---
   import { MyButton } from '@my-components/Button';
   ---
   
   <MyButton>Click me</MyButton>
   ```

## 最佳实践

1. **保持项目结构清晰**：避免引入过多外部文件夹，保持项目的模块化
2. **使用 TypeScript 路径别名**：提高代码的可读性和可维护性
3. **考虑使用 monorepo**：如果需要共享代码，考虑使用 pnpm workspace 或 Lerna
4. **测试构建流程**：确保引入外部文件夹后，构建流程仍然正常
5. **文档化依赖关系**：记录外部文件夹的引入方式和版本要求

## 常见问题

### Q: 引入外部文件夹后，TypeScript 报错？
A: 确保外部文件夹的 TypeScript 配置与当前项目兼容，或者在 `tsconfig.json` 的 `include` 中添加外部文件夹路径。

### Q: 构建时找不到外部文件？
A: 检查 Vite 别名配置是否正确，确保使用了 `new URL()` 语法或绝对路径。

### Q: 外部组件样式不生效？
A: 确保外部组件的样式导入方式与当前项目兼容，如使用 CSS Modules 或 Tailwind CSS。

## 总结

AstroPaper 项目可以通过多种方式引入其他文件夹的内容，包括：
- 相对路径
- 绝对路径
- TypeScript 路径别名
- Vite 别名配置

选择合适的方式取决于你的项目结构和需求。建议优先使用路径别名，以提高代码的可读性和可维护性。